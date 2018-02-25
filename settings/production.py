from .base import *

logging.log(logging.INFO, 'loading settings for ' + __name__)

DEBUG = False
TEMPLATE_DEBUG = False

MANAGERS = ('kellym@millcreeksoftware.biz',)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/webapp_cache',
        'TIMEOUT': 60,  # 60 seconds
    },
}
