# Django imports
from django import template
from django.template.defaultfilters import stringfilter

# My imports
from ..models import Post, Reply
from accounts.models import CustomUser


register = template.Library()


# Suggested users to follow
@register.simple_tag
def suggested_users(user):
    following = user.following
    users = CustomUser.objects.exclude(
        id__in=following.all()).exclude(id=user.id).order_by('?')[:10]
    return users


# Recent posts with hashtags
@register.simple_tag
def recent_hashtags():
    recent_hashtags = Post.objects.filter(
        post__contains='#')[:100]
    return recent_hashtags


# Count user mentions (for navigation badge)
@register.simple_tag
def mentions_count(user):
    posts = Post.objects.filter(
        post__icontains=user).exclude(read=user).count()
    replies = Reply.objects.filter(
        reply__icontains=user).exclude(hidden=True).exclude(
            read=user).count()
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
