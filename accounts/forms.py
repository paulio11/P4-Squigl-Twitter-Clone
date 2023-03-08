from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# Custom user creation form
class CustomUserCreationForm(UserCreationForm):

    # email = forms.EmailField(max_length=75, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Used in your profile URL and for logging in.'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'Pick a name to display on your profile.'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Used when you need to reset your password. Your email kept is private.'}
            )
        }


# Custom user change form
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'name',
            'about',
            'website',
            'avatar',
            'profile_background',
            )
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Pick a name to display on your profile.'}),
            'about': forms.TextInput(
                attrs={'placeholder': 'A place to share some information about yourself.'}),
            'website': forms.TextInput(
                attrs={'placeholder': 'Enter the FULL url of a website you would like to share.'}),
        }
