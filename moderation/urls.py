# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('moderation/', views.moderation, name='moderation'),
    path('mod-delete-post/<post_id>', views.mod_delete_post, name='mod_delete_post'),
]
