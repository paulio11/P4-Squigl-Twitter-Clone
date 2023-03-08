# Django imports
from django.db import models

# My imports
from accounts.models import CustomUser


class Message(models.Model):

    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='recipient')
    message = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Message from: {self.sender}, to: {self.recipient}'
