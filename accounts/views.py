# Django imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

# My imports
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# User sign up
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Edit user profile
class EditProfile(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('user', kwargs={
            'user': self.object
        })


# User settings
class UserSettings(UpdateView):
    model = CustomUser
    template_name = 'user-settings.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('feed')
