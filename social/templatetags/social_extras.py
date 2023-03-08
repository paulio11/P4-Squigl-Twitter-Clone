# Django imports
from django import template
from django.template.defaultfilters import stringfilter

# My imports
from ..models import Post, Reply


register = template.Library()


# Count user mentions (for navigation badge)
@register.simple_tag
def mentions_count(user):
    posts = Post.objects.filter(post__icontains=user).count()
    replies = Reply.objects.filter(
        reply__icontains=user).exclude(hidden=True).count()
    return posts + replies


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
