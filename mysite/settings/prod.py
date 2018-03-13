from .base import *

import dj_database_url

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# overide database settings
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)