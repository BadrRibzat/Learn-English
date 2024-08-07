from django.core.management.base import BaseCommand
from api.models import User, Lesson, UserProgress, Quiz, Achievement, UserAchievement

class Command(BaseCommand):
    help = 'Initialize the database with necessary collections'

    def handle(self, *args, **kwargs):
        # Create collections
        User.objects.first()
        Lesson.objects.first()
        UserProgress.objects.first()
        Quiz.objects.first()
        Achievement.objects.first()
        UserAchievement.objects.first()

        self.stdout.write(self.style.SUCCESS('Successfully initialized the database'))
