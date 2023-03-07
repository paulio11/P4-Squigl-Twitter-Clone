from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
