from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Feed
    path('feed/', views.feed, name='feed'),
    # Post
    path('post/<post_id>', views.post, name='post'),
    path('edit-post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('new-post/', views.new_post, name='new_post'),
    # User
    path('u/<user_username>', views.user, name='user'),
]
