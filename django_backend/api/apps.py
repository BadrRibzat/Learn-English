from django.apps import AppConfig
from django.db import connection

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Create collections when the app is ready
        from .models import User, Lesson, UserProgress, Quiz, Achievement, UserAchievement
        models = [User, Lesson, UserProgress, Quiz, Achievement, UserAchievement]
        for model in models:
            if model._meta.db_table not in connection.introspection.table_names():
                model.objects.create()
