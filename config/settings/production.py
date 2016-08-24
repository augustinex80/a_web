from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*', ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'a_web_db',
        'USER': 'a_web_local',
        'PASSWORD': '6789abc#',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}

# static root for collectstatic
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'a_web_static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'a_web_media')