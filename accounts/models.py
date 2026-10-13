from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Al heredar de AbstractUser, ya incluye campos como username, email, password, etc.
    pass

