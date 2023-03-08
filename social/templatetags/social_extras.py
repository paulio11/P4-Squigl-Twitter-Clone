# Django imports
from django import template
from django.template.defaultfilters import stringfilter

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


# Used to strip timesince down to just miunutes or hours
@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]


upto.is_safe = True
