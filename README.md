# English Learning Application

## Project Setup and Progress

### Step 1: Project Setup and Environment Configuration

[This section remains the same as in the previous response]

### Step 2: Define Data Models

[This section remains the same as in the previous response]

### Step 3: Implement API

1. Created serializers for the models in `django_backend/api/serializers.py`:
   - UserSerializer
   - LessonSerializer
   - FlashcardSerializer
   - UserProgressSerializer
   - QuizSerializer
   - QuizQuestionSerializer
   - AchievementSerializer
   - UserAchievementSerializer

2. Implemented API views in `django_backend/api/views.py`:
   - UserViewSet
   - LessonViewSet
   - FlashcardViewSet
   - UserProgressViewSet
   - QuizViewSet
   - QuizQuestionViewSet
   - AchievementViewSet
   - UserAchievementViewSet

3. Set up URL routing for the API in `django_backend/api/urls.py`:
   - Configured router for ViewSets
   - Added additional custom endpoints as needed

4. Configured main URL routing in `django_backend/config/urls.py`:
   - Included API URLs
   - Set up admin site
   - Configured Swagger and ReDoc for API documentation

### Step 4: Database Initialization

Created a custom management command `init_db.py` in `django_backend/api/management/commands/` to initialize the database with sample data.

### Step 5: Configure Django Settings

Updated `django_backend/config/settings.py`:
- Configured database settings for MongoDB
- Added REST framework settings
- Set up JWT authentication
- Configured CORS settings
- Added Swagger settings

### Step 6: Set Up Authentication

- Implemented JWT authentication using `djangorestframework-simplejwt`
- Created custom user model in `api/models.py`
- Updated admin site to use custom user model

## Current Project Structure

Learn-English/
├── django_backend/
│ ├── api/
│ │ ├── management/
│ │ │ └── commands/
│ │ │ └── init_db.py
│ │ ├── migrations/
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── tests.py
│ │ ├── urls.py
│ │ └── views.py
│ ├── config/
│ │ ├── asgi.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ └── manage.py
├── frontend/ # Currently under development
├── env/
├── README.md
└── requirements.txt

## Next Steps

1. Implement permissions for different user roles
2. Enhance API documentation using drf-yasg
3. Write unit tests for API endpoints
4. Implement additional features such as:
   - User registration and profile management
   - Lesson progression tracking
   - Quiz scoring and feedback
   - Achievement system
5. Integrate the API with the frontend (currently under development)

## Running the Project

To run the project:

1. Ensure MongoDB is installed and running
2. Activate the virtual environment:
   ```bash
   source env/bin/activate

3. Navigate to the django_backend directory:
   ```bash
   cd django_backend

4. Run the Django development server:
   ```bash
   python manage.py runserver

5.  Access the API endpoints at http://localhost:8000/api/

6. View API documentation:
Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

Note: The project is still in development, and these steps may change as we progress. The frontend is currently under development and will be integrated in future updates.

API Endpoints
The following API endpoints are currently available:

/api/users/: User management
/api/lessons/: Lesson management
/api/flashcards/: Flashcard management
/api/user-progress/: User progress tracking
/api/quizzes/: Quiz management
/api/quiz-questions/: Quiz question management
/api/achievements/: Achievement management
/api/user-achievements/: User achievement tracking
For detailed information on each endpoint, including available methods and required parameters, please refer to the Swagger or ReDoc documentation.

This README.md file will be updated during development process.
