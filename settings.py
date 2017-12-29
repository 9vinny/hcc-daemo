import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



DEBUG = True

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False

REGISTRATION_ALLOWED = True

CELERY_RESULT_BACKEND = 'redis://localhost:6379'
BROKER_URL = 'redis://localhost:6379'
CELERY_TIMEZONE = 'America/Los_Angeles'

SITE_HOST = 'https://localhost:8000'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
