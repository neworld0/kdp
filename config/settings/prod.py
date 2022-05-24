from .base import *
import os

ALLOWED_HOSTS = ['3.39.26.240', 'woori-life.co.kr', 'hiddenholdings.co.kr', 'hiddenholdings.kr']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEBUG = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]