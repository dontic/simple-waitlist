# django
from django.db import models
from django.contrib.auth.models import AbstractUser


# User model in case we want to add more fields in the future
class User(AbstractUser):
    pass
