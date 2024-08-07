from rest_framework import serializers
from .models import User, Lesson, UserProgress, Quiz, Achievement, UserAchievement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'native_language', 'current_level']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class FlashcardSerializer(serializers.Serializer):
    front_content = serializers.CharField()
    back_content = serializers.CharField()
    flashcard_type = serializers.ChoiceField(choices=['VOC', 'GRM', 'SEN'])

class LessonSerializer(serializers.ModelSerializer):
    flashcards = FlashcardSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['_id', 'title', 'description', 'level', 'order', 'flashcards']

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
