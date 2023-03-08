# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('', views.moderation, name='moderation'),
    path('delete-post/<post_id>', views.mod_delete_post, name='mod_delete_post'),
    path('delete-reply/<reply_id>', views.mod_delete_reply, name='mod_delete_reply'),
    path('post-okay/<post_id>', views.post_is_okay, name='mod_post_okay'),
    path('reply-okay/<reply_id>', views.reply_is_okay, name='mod_reply_okay'),
]
