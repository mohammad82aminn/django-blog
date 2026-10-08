# Django Blog

A simple blog built with Django while following a project-based Django course.

## Features (planned)

- Post list and post detail pages
- Create, update and delete posts (CRUD)
- Login, logout and sign up
- Tests for models and views

## Tech stack

- Python 3.12
- Django 6.1
- environs (environment variables)
- SQLite (development)

## Run locally

```bash
git clone https://github.com/<your-username>/django-blog.git
cd django-blog
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

Then put a real secret key in `.env`.