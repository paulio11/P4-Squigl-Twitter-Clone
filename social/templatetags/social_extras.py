# Django imports
from django import template

# My imports
from ..models import Reply


register = template.Library()


# Check if user has replied to a post
@register.simple_tag
def user_has_replied(user, post):
    replies = Reply.objects.filter(
        post=post).filter(user=user).exclude(hidden=True).count()
    if replies >= 1:
        return True
    else:
        return False
