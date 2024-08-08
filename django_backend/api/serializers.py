from rest_framework import serializers
from .models import User, Level, Lesson, Flashcard, UserProgress, Quiz, Achievement, UserAchievement
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'native_language')
        extra_kwargs = {
            'email': {'required': True},
            'native_language': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            native_language=validated_data['native_language']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'native_language', 'current_level']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['_id', 'name', 'description']

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['_id', 'lesson', 'front_content', 'back_content', 'flashcard_type', 'order']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['_id', 'level', 'title', 'brief', 'order']

class LessonDetailSerializer(serializers.ModelSerializer):
    flashcards = FlashcardSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['_id', 'level', 'title', 'brief', 'content', 'order', 'flashcards']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['_id', 'user', 'lesson', 'completed', 'score', 'last_studied']

class QuizQuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    correct_answer = serializers.CharField()
    option1 = serializers.CharField()
    option2 = serializers.CharField()
    option3 = serializers.CharField()

class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['_id', 'lesson', 'title', 'questions']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['_id', 'name', 'description', 'icon']

class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer(read_only=True)

    class Meta:
        model = UserAchievement
        fields = ['_id', 'user', 'achievement', 'date_earned']


