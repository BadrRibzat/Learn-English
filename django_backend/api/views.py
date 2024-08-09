from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
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


# Update the RegisterView
class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegisterSerializer, responses={201: UserSerializer()})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add a new view for login
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Update the LessonViewSet
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.request.user.is_authenticated:
            return LessonDetailSerializer
        return LessonSerializer

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def visitor(self, request):
        lessons = self.get_queryset()
        serializer = self.get_serializer(lessons, many=True)
        return Response(serializer.data)

# Update the QuizViewSet
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
