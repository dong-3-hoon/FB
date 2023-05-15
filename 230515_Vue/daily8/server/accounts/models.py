from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.TextField(unique=True)
    password = models.TextField()
