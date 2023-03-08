from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Custom user model
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, validators=[alphanumeric])
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    profile_background = models.ImageField(
        upload_to='backgrounds/', blank=True)
    about = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=50, blank=True)
    verified = models.BooleanField(default=False)
    following = models.ManyToManyField(
        'CustomUser', related_name='follower', blank=True)

    def __str__(self):
        return self.username

    def following_count(self):
        return self.following.count()

    def followers_count(self):
        return CustomUser.objects.filter(following=self.id).count()
