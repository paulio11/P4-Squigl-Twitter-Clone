from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Custom user model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    display_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    about = models.CharField(max_length=200, blank=True)
    verified = models.BooleanField(default=False)
    following = models.ManyToManyField(
        'self', related_name='following', blank=True)

    def __str__(self):
        return self.username
