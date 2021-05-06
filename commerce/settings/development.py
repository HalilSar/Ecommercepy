from commerce.settings.base import *

DEBUG = True
from pathlib import Path
import os
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT =os.path.join(BASE_DIR ,"static_cdn")
STATICFILES_DIRS = [
   os.path.join(BASE_DIR ,"static")
]
