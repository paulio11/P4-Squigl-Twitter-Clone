# Django imports
from django import template

# My imports
from ..models import Message


register = template.Library()


# Unread message count
@register.simple_tag
def unread_count(user):
    unread_messages = Message.objects.filter(
        recipient=user).filter(read=False)
    return unread_messages.count()