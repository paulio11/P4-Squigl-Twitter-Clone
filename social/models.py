# Django imports
from django.db import models

# Other imports
from django_resized import ResizedImageField
from datetime import datetime, timezone

# My imports
from accounts.models import CustomUser


class Post(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='post')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.TextField(max_length=400)
    image = ResizedImageField(
        upload_to='post-images/',
        blank=True,
        size=[600, None],
        force_format='WEBP')
    link = models.CharField(max_length=50, blank=True)
    likes = models.ManyToManyField(
        CustomUser, related_name='post_likes', blank=True)
    repost_post = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='repost',
        blank=True,
        null=True)
    reported = models.ManyToManyField(
        CustomUser, related_name='reported_post', blank=True)
    read = models.ManyToManyField(
        CustomUser, related_name='read_posts', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Post: {self.id}, by: {self.user}, on: {self.date}'

    def like_count(self):
        return self.likes.count()

    def reply_count(self):
        return Reply.objects.filter(post=self.id).exclude(hidden=True).count()

    def repost_count(self):
        return Post.objects.filter(repost_post=self).count()

    def reported_count(self):
        return self.reported.count()

    def time_check(self):
        now = datetime.now(timezone.utc)
        time_since = now - self.date
        hours_since = int(time_since.total_seconds() / 60 / 60)
        if hours_since < 24:
            less_than_a_day = True
        else:
            less_than_a_day = False
        return less_than_a_day


class Reply(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='reply')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reply')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reply = models.CharField(max_length=400)
    hidden = models.BooleanField(default=False)
    reported = models.ManyToManyField(
        CustomUser, related_name='reported_reply', blank=True)
    read = models.ManyToManyField(
        CustomUser, related_name='read_replies', blank=True)

    class Meta:
        ordering = ['post']
        verbose_name_plural = 'replies'

    def __str__(self):
        return f'Reply: {self.id}, for: {self.post}, by: {self.user}'

    def reported_count(self):
        return self.reported.count()

    def time_check(self):
        now = datetime.now(timezone.utc)
        time_since = now - self.date
        hours_since = int(time_since.total_seconds() / 60 / 60)
        if hours_since < 24:
            less_than_a_day = True
        else:
            less_than_a_day = False
        return less_than_a_day
