from djongo import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    _id = models.ObjectIdField()
    native_language = models.CharField(max_length=2, choices=[
        ('KO', _('Korean')),
        ('ZH', _('Chinese')),
        ('JA', _('Japanese')),
        ('FR', _('French')),
        ('ES', _('Spanish')),
        ('AR', _('Arabic')),
        ('DE', _('German'))
    ])
    current_level = models.CharField(max_length=3, choices=[
        ('BEG', _('Beginner')),
        ('INT', _('Intermediate')),
        ('ADV', _('Advanced'))
    ], default='BEG')

    # Override the groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    # Override the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    def __str__(self):
        return self.username

# The rest of your models remain unchanged
class Level(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=3, choices=[
        ('BEG', _('Beginner')),
        ('INT', _('Intermediate')),
        ('ADV', _('Advanced'))
    ])
    description = models.TextField()

class Lesson(models.Model):
    _id = models.ObjectIdField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    brief = models.TextField()  # Brief description visible to visitors
    content = models.TextField()  # Detailed content for registered users
    order = models.IntegerField()

    def __str__(self):
        return f"{self.level.name} - Lesson {self.order}: {self.title}"

class Flashcard(models.Model):
    _id = models.ObjectIdField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='flashcards')
    front_content = models.TextField()
    back_content = models.TextField()
    flashcard_type = models.CharField(max_length=3, choices=[
        ('VOC', _('Vocabulary')),
        ('GRM', _('Grammar')),
        ('SEN', _('Sentence'))
    ])
    order = models.IntegerField()

class UserProgress(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    score = models.FloatField(default=0.0)
    last_studied = models.DateTimeField(auto_now=True)

class Quiz(models.Model):
    _id = models.ObjectIdField()
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=200)
    questions = models.JSONField()  # Storing questions as JSON

class Achievement(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=255)  # Changed from ImageField to CharField

class UserAchievement(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_earned = models.DateTimeField(auto_now_add=True)

class ChatbotConversation(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatbot_conversations')
    timestamp = models.DateTimeField(auto_now_add=True)
    user_input = models.TextField()
    bot_response = models.TextField()
    intent = models.CharField(max_length=100)
    confidence = models.FloatField()

class TranslatedContent(models.Model):
    _id = models.ObjectIdField()
    content_type = models.CharField(max_length=50)  # e.g., 'lesson', 'flashcard', 'achievement'
    content_id = models.CharField(max_length=24)  # Store the ObjectId as a string
    language = models.CharField(max_length=2)
    field_name = models.CharField(max_length=50)  # e.g., 'title', 'description', 'front_content'
    translated_text = models.TextField()

    class Meta:
        unique_together = ('content_type', 'content_id', 'language', 'field_name')

