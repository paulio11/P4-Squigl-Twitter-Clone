# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My imports
from .models import CustomUser


admin.site.register(CustomUser)
