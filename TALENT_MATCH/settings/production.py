import os
from .base import *

DEBUG = False

# En producción no hay valores por defecto, se lee estrictamente del .env real
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Configuraciones de seguridad obligatorias para servidores en producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
