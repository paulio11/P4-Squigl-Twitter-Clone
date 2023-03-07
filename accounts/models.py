from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
