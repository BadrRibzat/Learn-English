from django.core.management.base import BaseCommand
from api.models import User, Level, Lesson, Flashcard, Quiz, Achievement
from django.db import transaction
from django.contrib.auth.hashers import make_password
from collections import defaultdict

class Command(BaseCommand):
    help = 'Initialize the database with sample data'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Initializing database...')

        try:
            # Create a superuser
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
                self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS('Superuser already exists'))

            # Create levels
            levels = {
                'BEG': 'Beginner level',
                'INT': 'Intermediate level',
                'ADV': 'Advanced level'
            }
            for name, description in levels.items():
                Level.objects.get_or_create(name=name, defaults={'description': description})
            self.stdout.write(self.style.SUCCESS('Levels created successfully'))

            # Create lessons for beginner level
            beginner = Level.objects.get(name='BEG')
            lessons = [
                {
                    'title': "Basic Greetings and Introductions",
                    'brief': "Learn how to greet people and introduce yourself in English.",
                    'content': "Detailed content for registered users...",
                    'order': 1
                },
                {
                    'title': "Numbers and Simple Counting",
                    'brief': "Master numbers from 1 to 100 and basic counting skills.",
                    'content': "Detailed content for registered users...",
                    'order': 2
                },
                {
                    'title': "Days of the Week and Telling Time",
                    'brief': "Learn the days of the week and how to tell time in English.",
                    'content': "Detailed content for registered users...",
                    'order': 3
                },
                {
                    'title': "Family Members and Basic Descriptions",
                    'brief': "Vocabulary for family members and simple descriptive words.",
                    'content': "Detailed content for registered users...",
                    'order': 4
                },
                {
                    'title': "Common Objects and Colors",
                    'brief': "Learn names of everyday objects and colors.",
                    'content': "Detailed content for registered users...",
                    'order': 5
                },
                {
                    'title': "Simple Present Tense: Daily Routines",
                    'brief': "Introduction to simple present tense using daily activities.",
                    'content': "Detailed content for registered users...",
                    'order': 6
                },
                {
                    'title': "Basic Food and Drink Vocabulary",
                    'brief': "Learn common food and drink names and simple ordering phrases.",
                    'content': "Detailed content for registered users...",
                    'order': 7
                },
                {
                    'title': "Simple Questions and Answers",
                    'brief': "Practice forming and responding to basic questions in English.",
                    'content': "Detailed content for registered users...",
                    'order': 8
                },
                {
                    'title': "Basic Adjectives and Comparisons",
                    'brief': "Introduction to common adjectives and making simple comparisons.",
                    'content': "Detailed content for registered users...",
                    'order': 9
                },
                
                {
                    'title': "Simple Past Tense: Talking about Yesterday",
                    'brief': "Learn to talk about past events using simple past tense.",
                    'content': "Detailed content for registered users...",
                    'order': 10
                }
            ]

            # Check for existing lessons and handle duplicates
            existing_lessons = list(Lesson.objects.filter(level=beginner).values('_id', 'order'))
            order_count = defaultdict(int)
            lessons_to_keep = {}
            lessons_to_delete = []

            for lesson in existing_lessons:
                order_count[lesson['order']] += 1
                if order_count[lesson['order']] == 1:
                    lessons_to_keep[lesson['order']] = lesson['_id']
                else:
                    lessons_to_delete.append(lesson['_id'])

            if lessons_to_delete:
                self.stdout.write(self.style.WARNING('Duplicate lessons found. Cleaning up...'))
                Lesson.objects.filter(_id__in=lessons_to_delete).delete()
                self.stdout.write(self.style.SUCCESS('Duplicate lessons cleaned up'))

            # Create or update lessons
            for lesson_data in lessons:
                lesson, created = Lesson.objects.update_or_create(
                    level=beginner,
                    order=lesson_data['order'],
                    defaults={
                        'title': lesson_data['title'],
                        'brief': lesson_data['brief'],
                        'content': lesson_data['content'],
                    }
                )
                if created:
                    self.stdout.write(f"Created lesson: {lesson.title}")
                else:
                    self.stdout.write(f"Updated lesson: {lesson.title}")

            self.stdout.write(self.style.SUCCESS('Lessons processed successfully'))

            # Create flashcards for the first lesson
            lesson1 = Lesson.objects.get(level=beginner, order=1)
            flashcards = [
                {
                    'front_content': "Hello",
                    'back_content': "A common greeting",
                    'flashcard_type': 'VOC',
                    'order': 1
                },
                {
                    'front_content': "My name is...",
                    'back_content': "Used to introduce yourself",
                    'flashcard_type': 'SEN',
                    'order': 2
                }
            ]
            for flashcard_data in flashcards:
                Flashcard.objects.update_or_create(
                    lesson=lesson1,
                    order=flashcard_data['order'],
                    defaults={
                        'front_content': flashcard_data['front_content'],
                        'back_content': flashcard_data['back_content'],
                        'flashcard_type': flashcard_data['flashcard_type'],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Flashcards processed successfully'))

            # Create a quiz for the first lesson
            Quiz.objects.update_or_create(
                lesson=lesson1,
                defaults={
                    'title': "Greetings Quiz",
                    'questions': [
                        {
                            'question': 'What is a common greeting in English?',
                            'options': ['Hello', 'Goodbye', 'Thank you', 'Sorry'],
                            'correct_answer': 'Hello'
                        },
                        {
                            'question': 'How do you introduce yourself?',
                            'options': ['My name is...', 'I am...', 'Both A and B', 'Neither'],
                            'correct_answer': 'Both A and B'
                        }
                    ]
                }
            )
            self.stdout.write(self.style.SUCCESS('Quiz processed successfully'))

            # Create an achievement
            Achievement.objects.update_or_create(
                name="First Lesson Completed",
                defaults={
                    'description': "You've completed your first lesson!",
                    'icon': "achievement_icons/first_lesson.png"
                }
            )
            self.stdout.write(self.style.SUCCESS('Achievement processed successfully'))

            self.stdout.write(self.style.SUCCESS('Successfully initialized the database with sample data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            raise  # Re-raise the exception to see the full traceback
