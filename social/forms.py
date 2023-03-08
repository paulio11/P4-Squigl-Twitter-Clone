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
            'post': forms.Textarea(
                attrs={'placeholder': 'Use ~ to tag a ~username, or # to create a #hashtag.'}),
            'link': forms.TextInput(
                attrs={'placeholder': 'Enter the FULL url. Example: https://www.squigl.com/'})
        }


# Reply form
class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']
        widgets = {
            'reply': forms.Textarea(attrs={
                'class': 'reply-input',
                'aria-label': 'reply',
                'placeholder': 'Type your reply here.',
                'rows': '4',
            }),
        }
