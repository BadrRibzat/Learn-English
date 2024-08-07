### Updated README.md

# English Learning Application

## Project Setup and Progress

### Project Setup

To set up the English Learning Application, follow these steps:

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.8 or higher**: You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer (should be included with Python).
- **MongoDB**: You can download it from [mongodb.com](https://www.mongodb.com/try/download/community).
- **Git**: To clone the repository. Download from [git-scm.com](https://git-scm.com/downloads).

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/BadrRibzat/Learn-English.git

# Navigate into the project directory:
cd Learn-English

Step 2: Set Up a Virtual Environment
As it is recommended to create a virtual environment to manage project dependencies.
 
Run the following commands:
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment named 'env'
virtualenv env

# Activate the virtual environment
# On macOS and Linux:
source env/bin/activate
# On Windows:
# env\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Configure MongoDB
Ensure that MongoDB is installed and running on your machine. You can start the MongoDB server with the following commands:

mongod or mongo or mongosh

If you need to set up a database for your application, you can do so using the MongoDB shell or a GUI tool like MongoDB Compass.

create the .env file in the django_backend directory to store sensitives secrets keys and database string and other information as required.
You can use the following template:

# .env file template
DEBUG=True
SECRET_KEY=your_secret_key
MONGODB_URI=mongodb://localhost:27017/your_database_name



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

## Current Project Tree Structure for the django_backend:

```plaintext
django_backend/
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── chatbot.py
│   ├── db.py
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   │       ├── init_db.py
│   │       └── __pycache__
│   │           └── init_db.cpython-310.pyc
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── chatbot.cpython-310.pyc
│   │   ├── db.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── locale
│   ├── ar
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   ├── de
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   ├── es
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   ├── ja
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   ├── ko
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   └── zh
│       └── LC_MESSAGES
│           ├── django.mo
│           └── django.po
└── manage.py
```

## Next Steps

1. Implement permissions for different user roles.
2. Enhance API documentation using drf-yasg.
3. Write unit tests for API endpoints.
4. Implement additional features such as:
   - User registration and profile management.
   - Lesson progression tracking.
   - Quiz scoring and feedback.
   - Achievement system.
5. Integrate the API with the frontend (currently under development).

## Running the Project

To run the project:

1. Ensure MongoDB is installed and running.
2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
3. Navigate to the `django_backend` directory:
   ```bash
   cd django_backend
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Access the API endpoints at `http://localhost:8000/api/`.
6. View API documentation:
   - Swagger UI: `http://localhost:8000/swagger/`
   - ReDoc: `http://localhost:8000/redoc/`

**Note:** The project is still in development, and these steps may change as we progress. The frontend is currently under development and will be integrated in future updates.

## API Endpoints

The following API endpoints are currently available:

- `/api/users/`: User management
- `/api/lessons/`: Lesson management
- `/api/flashcards/`: Flashcard management
- `/api/user-progress/`: User progress tracking
- `/api/quizzes/`: Quiz management
- `/api/quiz-questions/`: Quiz question management
- `/api/achievements/`: Achievement management
- `/api/user-achievements/`: User achievement tracking

For detailed information on each endpoint, including available methods and required parameters, please refer to the Swagger or ReDoc documentation.

This README.md file will be updated during the development process.
```

### Key Changes Made

1. **Corrected Project Tree Structure**: Updated the project tree structure to match the one shown in your GitHub repository, ensuring that all file names and directories are accurate.
  
2. **Formatting Improvements**: Ensured consistent formatting throughout the document for better readability.

3. **Clarifications**: Added minor clarifications in the "Running the Project" section and the "Next Steps" section.

### Next Steps

1. **Update Your README.md**: Replace the existing content in your `README.md` file with the updated version above.

2. **Commit Your Changes**: After updating the file, don't forget to stage, commit, and push your changes to the remote repository:

