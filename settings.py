import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = 'django-insecure-!8s42u$(i$*5c$rx$u1q8rsfm@j3$=*^9jr@+85678#k-=rwvw'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

USE_TZ = False

INSTALLED_APPS = ("app",)
