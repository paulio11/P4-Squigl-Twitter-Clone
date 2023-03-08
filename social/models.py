# Django imports
from django.db import models

# My imports
from accounts.models import CustomUser


class Post(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='post')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.TextField(max_length=400)
    image = models.ImageField(upload_to='post-images/', blank=True)
    link = models.CharField(max_length=50, blank=True)
    likes = models.ManyToManyField(
        CustomUser, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Post: {self.id}, by: {self.user}, on: {self.date}'

    def likes_count(self):
        return self.likes.count()


class Reply(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='reply')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reply')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reply = models.CharField(max_length=400)

    class Meta:
        ordering = ['post']
        verbose_name_plural = 'replies'

    def __str__(self):
        return f'Reply: {self.id}, for: {self.post}, by: {self.user}'
