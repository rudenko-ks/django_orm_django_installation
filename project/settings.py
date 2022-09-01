import os
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env("HOST"),
        'PORT': env.int("PORT"),
        'NAME': env("NAME"),
        'USER': env("USER"),
        'PASSWORD': env("PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", True)

ROOT_URLCONF = env("ROOT_URLCONF")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = env.bool("USE_L10N", True)

LANGUAGE_CODE = env("LANGUAGE_CODE")

TIME_ZONE = env("TIME_ZONE")

USE_TZ = env.bool("USE_TZ", True)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
