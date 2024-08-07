from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, LessonViewSet, UserProgressViewSet,
    QuizViewSet, AchievementViewSet, UserAchievementViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'progress', UserProgressViewSet, basename='userprogress')
router.register(r'quizzes', QuizViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'user-achievements', UserAchievementViewSet, basename='userachievement')

urlpatterns = [
    path('', include(router.urls)),
]
