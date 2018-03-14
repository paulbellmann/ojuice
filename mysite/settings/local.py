from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += 'debug_toolbar.middleware.DebugToolbarMiddleware',
INTERNAL_IPS = ['localhost', '127.0.0.1']