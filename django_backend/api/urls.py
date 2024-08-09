from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, LevelViewSet, LessonViewSet, FlashcardViewSet,
    UserProgressViewSet, QuizViewSet, AchievementViewSet, UserAchievementViewSet,
    chatbot, RegisterView, LoginView, UserProfileView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'flashcards', FlashcardViewSet)
router.register(r'progress', UserProgressViewSet, basename='userprogress')
router.register(r'quizzes', QuizViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'user-achievements', UserAchievementViewSet, basename='userachievement')

urlpatterns = [
    path('', include(router.urls)),
    path('chatbot/', chatbot, name='chatbot'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
]
