"""
Django settings for sigssmac_proyecto project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", '&2(_fsb8myf6jx4(3i9w3v8o-hy@h0u80k!msdf_azr(2*d9tr')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG")) == "1"

ENV_ALLOWED_HOST = os.environ.get("DJANGO_ALLOWED_HOST") or None
ALLOWED_HOSTS = []
ALLOWED_HOSTS += [os.environ.get("DJANGO_ALLOWED_HOST")]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "sigss_principal.apps.SigssPrincipalConfig",
    'guardian',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sigssmac_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

WSGI_APPLICATION = 'sigssmac_proyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_NAME"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'HOST': os.environ.get("MYSQL_HOST"),
        'PORT': os.environ.get("MYSQL_PORT"),
    },
    'sigssmac_db': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'NAME': os.environ.get("MYSQL_NAME"),
        'PORT': os.environ.get("MYSQL_PORT"),
    },
    'api_energy_db': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'NAME': os.environ.get("MYSQL_NAME2"),
        'PORT': os.environ.get("MYSQL_PORT"),
    },
    'mcgreen_db': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'NAME': os.environ.get("MYSQL_NAME3"),
        'PORT': os.environ.get("MYSQL_PORT"),
    },
    'tarco_db': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("MYSQL_HOST"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'NAME': os.environ.get("MYSQL_NAME4"),
        'PORT': os.environ.get("MYSQL_PORT"),
    }
}

DATABASE_ROUTERS = ['routers.routers.SigssmacRouter', 'routers.routers.TarcoRouter', 'routers.routers.ApiEnergyRouter', 'routers.routers.McGreenRouter']


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', "zaailyeddrycxcbu")
RECIPIENT_ADDRESS = os.environ.get('RECIPIENT_ADDRESS')

LOGIN_URL = 'inicio_sesion'
LOGIN_REDIRECT_URL = '/tarco'
LOGOUT_URL = 'cerrar_sesion'
LOGOUT_REDIRECT_URL = '/tarco'

STATIC_ROOT = str(os.environ.get("ALLOWED_HOSTS")) + "/static/"
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'