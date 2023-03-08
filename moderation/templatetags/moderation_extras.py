# Django imports
from django import template
from django.db.models import Count

# My imports
from social.models import Post, Reply
from dm.models import Message


register = template.Library()


# Moderation count
@register.simple_tag
def mod_count():
    reported_posts = Post.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0).count()
    reported_replies = Reply.objects.annotate(
        nreports=Count('reported')).filter(nreports__gt=0).count()
    reported_messages = Message.objects.filter(reported=True).count()
    return reported_posts + reported_replies + reported_messages
