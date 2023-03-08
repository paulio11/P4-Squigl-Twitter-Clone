# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

# Other imports
from django_resized import ResizedImageField


# My validators
alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Custom user model
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, validators=[alphanumeric])
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    avatar = ResizedImageField(
        upload_to='avatars/',
        blank=True,
        size=[150, 150],
        crop=['middle', 'center'],
        force_format='JPEG')
    profile_background = ResizedImageField(
        upload_to='backgrounds/',
        blank=True,
        size=[600, 200],
        crop=['middle', 'center'],
        force_format='JPEG')
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
