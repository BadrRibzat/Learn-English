from djongo import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    _id = models.ObjectIdField()
    LANGUAGE_CHOICES = [
        ('KO', 'Korean'),
        ('ZH', 'Chinese'),
        ('JA', 'Japanese'),
        ('ES', 'Spanish'),
        ('AR', 'Arabic'),
        ('DE', 'German'),
    ]
    LEVEL_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    ]
    
    native_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    current_level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='BEG')
    
    def __str__(self):
        return self.username

class Flashcard(models.Model):
    FLASHCARD_TYPES = [
        ('VOC', 'Vocabulary'),
        ('GRM', 'Grammar'),
        ('SEN', 'Sentence'),
    ]

    
    front_content = models.TextField()
    back_content = models.TextField()
    flashcard_type = models.CharField(max_length=3, choices=FLASHCARD_TYPES)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.get_flashcard_type_display()} - {self.front_content[:30]}"

class Lesson(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=3, choices=User.LEVEL_CHOICES)
    order = models.IntegerField()
    flashcards = models.ArrayField(model_container=Flashcard)

    def __str__(self):
        return f"{self.get_level_display()} - {self.title}"

class UserProgress(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, related_name='progress', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='user_progress', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.FloatField(default=0.0)
    last_studied = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {'Completed' if self.completed else 'In Progress'}"

class QuizQuestion(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.question[:50]

class Quiz(models.Model):
    _id = models.ObjectIdField()
    lesson = models.OneToOneField(Lesson, related_name='quiz', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    questions = models.ArrayField(model_container=QuizQuestion)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"

class Achievement(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.name

class UserAchievement(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, related_name='achievements', on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_earned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'achievement']

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"
