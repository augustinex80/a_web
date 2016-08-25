from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*', ]

# db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
