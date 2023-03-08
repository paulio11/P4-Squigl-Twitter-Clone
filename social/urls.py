from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Feed
    path('feed/', views.feed, name='feed'),
    # Post
    path('post/<post_id>', views.post, name='post'),
    # User
    path('u/<user_username>', views.user, name='user'),
]
