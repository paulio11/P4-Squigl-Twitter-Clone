# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My imports
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['username', 'email']


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
