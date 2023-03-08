# Django imports
from django import forms

# My imports
from .models import Reply


# Reply form
class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']
        labels = {
            'reply': '',
        }
        widgets = {
            'reply': forms.TextInput(attrs={
                'class': 'reply-input',
                'placeholder': 'Type your reply here...',
            }),
        }
