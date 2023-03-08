# Django imports
from django.contrib import admin

# My imports
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date']
    ordering = ['id']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'hidden']
    ordering = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
