from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Registramos el modelo personalizado utilizando la interfaz de administración estándar de usuarios
admin.site.register(User, UserAdmin)
