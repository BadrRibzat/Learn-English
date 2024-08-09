from rest_framework import serializers
from .models import User, Level, Lesson, Flashcard, UserProgress, Quiz, Achievement, UserAchievement
from django.contrib.auth.password_validation import validate_password
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

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
        validated_data.pop('password2', None)
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'native_language', 'current_level']
        extra_kwargs = {'password': {'write_only': True}}

class LevelSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Level
        fields = ['_id', 'name', 'description']

class FlashcardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Flashcard
        fields = ['_id', 'lesson', 'front_content', 'back_content', 'flashcard_type', 'order']

class LessonSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Lesson
        fields = ['_id', 'level', 'title', 'brief', 'order']

class LessonDetailSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    flashcards = FlashcardSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['_id', 'level', 'title', 'brief', 'content', 'order', 'flashcards']

class UserProgressSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = UserProgress
        fields = ['_id', 'user', 'lesson', 'completed', 'score', 'last_studied']

class QuizQuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    options = serializers.ListField(child=serializers.CharField())
    correct_answer = serializers.CharField()

class QuizSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    questions = QuizQuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['_id', 'lesson', 'title', 'questions']

class AchievementSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Achievement
        fields = ['_id', 'name', 'description', 'icon']

class UserAchievementSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    achievement = AchievementSerializer(read_only=True)

    class Meta:
        model = UserAchievement
        fields = ['_id', 'user', 'achievement', 'date_earned']
