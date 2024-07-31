# Web-Stack Portfolio Project Final Full-Stack Project

```markdown
# English Learning Application

## Project Setup and Progress

### Step 1: Project Setup and Environment Configuration

1. Created project directory structure:
   ```
   Learn-English/
   ├── django_backend/
   │   ├── api/
   │   ├── config/
   │   └── manage.py
   ├── frontend/
   ├── env/
   ├── README.md
   └── requirements.txt
   ```

2. Set up virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Installed dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Key packages installed:
   - Django 5.0.7
   - Django Rest Framework 3.15.2
   - djongo 1.2.31 (MongoDB connector for Django)
   - djangorestframework-simplejwt 5.3.1
   - drf-yasg 1.21.7 (for API documentation)
   - Other supporting packages (see requirements.txt for full list)

4. Configured Django project settings in `django_backend/config/settings.py`:
   - Added installed apps
   - Configured database for MongoDB
   - Set up REST Framework and JWT settings
   - Configured CORS settings

### Step 2: Define Data Models

Created `django_backend/api/models.py` with the following models:

1. User (extends AbstractUser)
2. Lesson
3. Flashcard
4. UserProgress
5. Quiz
6. QuizQuestion
7. Achievement
8. UserAchievement

Models are designed to work with MongoDB using djongo fields where appropriate.

## Next Steps

The next phase of development will involve:

1. Creating serializers for the defined models
2. Implementing API views and endpoints
3. Setting up URL routing for the API
4. Implementing authentication and permissions
5. Creating API documentation using drf-yasg

## Running the Project

To run the project:

1. Ensure MongoDB is installed and running
2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
3. Navigate to the django_backend directory:
   ```bash
   cd django_backend
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

Note: The project is still in development, and these steps may change as we progress.

```

This README provides a good overview of what we've accomplished so far and outlines the next steps. You can save this content in a file named `README.md` in your project's root directory. 

