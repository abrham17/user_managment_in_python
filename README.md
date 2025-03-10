                User Management System
                
A Django-based user management system with email verification, password reset, and profile management.

                Key Features
                
- User registration with email verification (now working in the terminal only not email address)
- Secure login/logout functionality
- Password reset via email
- Profile management (update info & password)
- Email verification system with 6-digit codes

  steps
clone git repo  
                     git clone "https://github.com/abrham17/user_managment_in_python"
navigate to the repo

                     cd user_managment_in_python/signupform
  
install virtual environoment

                     pip install virtualenv
                     virtualenv .venv
                     .venv/Scripts/activate
  
install the neccessary libraries
                     pip install django
                     pip install python-dotenv
migrate file
                    python manage.py makemigrations
                    python manage.py migrate
run the web server
                    python manage.py runserver


project file structure

                        user_management/
                        ├── signupform/ # Django project root
                        │ ├── pycache/
                        │ ├── init.py
                        │ ├── asgi.py
                        │ ├── settings.py # Project configurations
                        │ ├── urls.py # Main URL routing
                        │ └── wsgi.py
                        │
                        ├── signup/ # User management app
                        │ ├── migrations/ # Database migrations
                        │ ├── templates/ # HTML templates
                        │ │ ├── forgot_password.html
                        │ │ ├── home.html
                        │ │ ├── login.html
                        │ │ ├── profile.html
                        │ │ ├── signup.html
                        │ │ ├── update_password.html
                        │ │ └── verify_code.html
                        │ │
                        │ ├── init.py
                        │ ├── admin.py
                        │ ├── apps.py
                        │ ├── forms.py # Custom forms
                        │ ├── models.py # Database models
                        │ ├── tests.py
                        │ ├── urls.py # App-specific routes
                        │ └── views.py # Business logic
                        │
                        ├── .venv/ # Virtual environment
                        ├── db.sqlite3 # Database file
                        └── manage.py # Django CLI tool



  
