# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My imports
from .models import CustomUser


@admin.action(description='Mark user as verified')
def verify_user(modeladmin, request, queryset):
    queryset.update(verified=True)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'verified']
    ordering = ['username']
    actions = [verify_user]


admin.site.register(CustomUser, CustomUserAdmin)
