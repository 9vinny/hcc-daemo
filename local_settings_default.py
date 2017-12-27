DEBUG = True

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False

REGISTRATION_ALLOWED = True

CELERY_RESULT_BACKEND = 'redis://localhost:6379'
BROKER_URL = 'redis://localhost:6379'
CELERY_TIMEZONE = 'America/Los_Angeles'

SITE_HOST = 'https://localhost:8000'

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "crowdsource_dev",
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crowdsource_dev',
        'USER': 'postgres',
        'PASSWORD': 'Learner#12',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
