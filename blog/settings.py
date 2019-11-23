import os
from .secret import SECRET_KEY
from .secret import (
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD
)
from configurations import Configuration


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ALLOWED_HOSTS = []

    INTERNAL_IPS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'crispy_forms',
        'debug_toolbar',
        'rest_framework',

        'main_page.apps.MainPageConfig',
        'users.apps.UsersConfig',
        'posts_api_v1.apps.PostsApiV1Config'

    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',

    ]

    ROOT_URLCONF = 'blog.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    WSGI_APPLICATION = 'blog.wsgi.application'

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
            'posts_api_v1.pagination.LimitOffsetPaginationWithMaxLimit',
        'PAGE_SIZE': 5,
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        )
    }

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

    LOGIN_REDIRECT_URL = 'blog-home'

    LOGIN_URL = 'login'


class Local(Base):
    DEBUG = True

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    SECRET_KEY = SECRET_KEY

    MEDIA_URL = '/media/'

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.BASE_DIR, 'media')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_HOST = 'smtp.gmail.com'

    EMAIL_PORT = 587

    EMAIL_USE_TLS = True

    EMAIL_HOST_USER = EMAIL_HOST_USER

    EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD


class Production(Base):
    DEBUG = False

    SECRET_KEY = SECRET_KEY

    ALLOWED_HOSTS = [
        'localhost'
    ]

    MEDIA_URL = '/media/'

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.BASE_DIR, 'media')
