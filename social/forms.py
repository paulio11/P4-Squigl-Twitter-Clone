# Django imports
from django import forms

# My imports
from .models import Reply


# Reply form
class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']
        widgets = {
            'reply': forms.TextInput(attrs={
                'class': 'reply-input',
                'aria-label': 'reply',
                'placeholder': 'Type your reply here...',
            }),
        }
