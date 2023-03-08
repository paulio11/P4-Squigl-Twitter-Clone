# Django imports
from django import forms

# My imports
from .models import Message


# Send message form
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['message']
