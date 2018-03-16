import os
import dj_database_url

IS_DEPLOYED = os.environ.get('is_deployed', 'False')

if IS_DEPLOYED == 'True':
    DATABASE_DICT = dj_database_url.config(default=os.environ.get('DATABASE_URL', ''))
else:
    DATABASE_DICT = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'VisualTesting',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
