from django.contrib import admin
from .models import User, Lesson, UserProgress, Quiz, Achievement, UserAchievement

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(UserProgress)
admin.site.register(Quiz)
admin.site.register(Achievement)
admin.site.register(UserAchievement)
