from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from google.cloud import translate_v2 as translate
from .models import User, Level, Lesson, Flashcard, UserProgress, Quiz, Achievement, UserAchievement
from .serializers import (
    UserSerializer, LevelSerializer, LessonSerializer, LessonDetailSerializer, FlashcardSerializer, UserProgressSerializer,
    QuizSerializer, AchievementSerializer, UserAchievementSerializer, RegisterSerializer
)
from .chatbot import get_chatbot_response
from google.auth.exceptions import DefaultCredentialsError
from google.api_core.exceptions import GoogleAPICallError

# Initialize the translation client
translate_client = translate.Client()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegisterSerializer, responses={201: UserSerializer()})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(responses={200: LessonSerializer(many=True)})
    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        level = self.get_object()
        serializer = LessonSerializer(level.lessons.all(), many=True)
        return Response(serializer.data)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.request.user.is_authenticated:
            return LessonDetailSerializer
        return LessonSerializer

    @swagger_auto_schema(responses={200: FlashcardSerializer(many=True)})
    @action(detail=True, methods=['get'])
    def flashcards(self, request, pk=None):
        lesson = self.get_object()
        serializer = FlashcardSerializer(lesson.flashcards.all(), many=True)
        return Response(serializer.data)

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAdminUser]

class UserAchievementViewSet(viewsets.ModelViewSet):
    serializer_class = UserAchievementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserAchievement.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([AllowAny])
def visitor_lessons(request):
    try:
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def chatbot(request):
    print("Received chatbot request")
    print(f"Request data: {request.data}")
    user_message = request.data.get('message')
    session_id = request.session.session_key or 'anonymous'

    print(f"Session ID: {session_id}")
    print(f"User message: {user_message}")
    
    if not user_message:
        return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Detect the language
        try:
            detection = translate_client.detect_language(user_message)
            detected_language = detection['language']
            print(f"Detected language: {detected_language}")
        except (DefaultCredentialsError, GoogleAPICallError) as e:
            print(f"Error detecting language: {str(e)}")
            detected_language = 'en'  # Default to English if detection fails
        
        # Get chatbot response
        chatbot_response = get_chatbot_response(session_id, user_message, detected_language)
        print(f"Chatbot response: {chatbot_response}")
        
        return Response({
            'response': chatbot_response,
            'detected_language': detected_language
        })
    except Exception as e:
        print(f"Error in chatbot view: {str(e)}")
        return Response({
            'error': 'An error occurred while processing your request',
            'details': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
