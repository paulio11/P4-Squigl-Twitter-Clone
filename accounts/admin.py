# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# My imports
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'verified', 'is_active']
    ordering = ['username']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
