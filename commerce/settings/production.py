from commerce.settings.base import *
import os

DEBUG = False
# Şimdilik db.sqlite3 kullanabiliriz.
ALLOWED_HOSTS = ['www.halil37pythonanywhere.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT =os.path.join(BASE_DIR ,"static")
