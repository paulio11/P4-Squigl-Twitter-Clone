# Django imports
from django.contrib import admin

# My imports
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sending', 'recipient', 'date']
    ordering = ['date']


admin.site.register(Message, MessageAdmin)
