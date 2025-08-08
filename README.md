# 📝 Personal Blog with Django

This is a simple personal blog built using Django. It allows writing, publishing, editing, and deleting articles through an admin section. Visitors can browse published articles on the main blog page.


https://roadmap.sh/projects/personal-blog


##  Features

###  Guest Section (Public)
- **Home Page**: Displays a list of all published articles.
- **Article Page**: Shows the full content of an article with its title and publication date.
- **Login Page**
- **Register Page**

###  Admin Section (Private)
- **Login Page**: Basic authentication to access the admin panel.
- **Dashboard**: List of all articles with options to add, edit, or delete them.
- **Add Article**: Form with fields for title, content, and publication date.
- **Edit Article**: Form to update article content.
- **Delete Article**: Option to remove an article from the database.

## ⚙️ Technical Overview

- Backend: **Django**
- Database: **SQLite** (default, can be changed)
- Templates: Django’s template engine (HTML + CSS)
- Authentication: Custom login system with session-based access

## Usage


Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create superuser (for admin access):
python manage.py createsuperuser

Start the server:
```bash
python manage.py runserver
