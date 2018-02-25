from .base import *

logging.log(logging.INFO, 'loading settings for ' + __name__)

DEBUG = True
DEVELOPMENT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wff',
        'USER': 'tim',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

SESSION_COOKIE_AGE = 7200
SESSION_EXPIRE_AT_BROWSER_CLOSE = False