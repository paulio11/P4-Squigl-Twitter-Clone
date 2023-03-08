# Django imports
from django import forms

# My imports
from .models import Post, Reply


# New post form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post', 'link', 'image']
        widgets = {
            'link': forms.TextInput(
                attrs={'placeholder': 'Enter the FULL url'})
        }


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
