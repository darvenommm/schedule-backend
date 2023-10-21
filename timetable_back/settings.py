import os
from datetime import timedelta
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)-@w44_a%dkm!uy6icb0#!0$x3jv(8zytuh)-$yrup5%(cg3_a'

DEBUG = True

ALLOWED_HOSTS = [
    'http://localhost:5173',
    '127.0.0.1',
    'localhost',
                 ]

# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:5173',
# )

# CORS_ALLOW_CREDENTIALS = True

LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = 'login'

INSTALLED_APPS = [
    'timetable_back_app',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# SOCIALACCOUNT_PROVIDERS = {
#     'github': {
#         'SCOPE': [
#             'user',
#             'repo',
#             'read:org',
#         ],
#         'APP': {
#             'client_id': '1ba9607aaa7690399da2',
#             'secret': 'afaf3e3f428086388f3f9efa9789d86177d37fb4',
#             'key': ''
#         }
#     }
# }


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',                          # <<< newly added line
]

GITHUB_CLIENT_ID = '1ba9607aaa7690399da2'
SOCIAL_SECRET = 'afaf3e3f428086388f3f9efa9789d86177d37fb4'

ROOT_URLCONF = 'timetable_back.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'timetable_back.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PG_DBNAME'),
        'USER': getenv('PG_USER'),
        'PASSWORD': getenv('PG_PASSWORD'),
        'HOST': getenv('PG_HOST'),
        'PORT': getenv('PG_PORT'),
        'TEST': {
            'NAME': 'test'
        }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    'templates/static/',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}
