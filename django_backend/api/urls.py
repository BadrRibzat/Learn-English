from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import (
    UserViewSet, LevelViewSet, LessonViewSet, FlashcardViewSet,
    UserProgressViewSet, QuizViewSet, AchievementViewSet, UserAchievementViewSet,
    chatbot, RegisterView, visitor_lessons, UserProfileView
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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('lessons/visitor/', visitor_lessons, name='visitor_lessons'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
]
