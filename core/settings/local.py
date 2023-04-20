from .base import *

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
SECRET_KEY = env(
    "DJANGO_SECRET",
    default="django-insecure-@mjmu07w^s8hsz1%t8n+a8zuizni21e87m5qq8x0z5d9qptj13",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db.sqlite3",
    }
}
