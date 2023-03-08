from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Feed
    path('feed/', views.feed, name='feed'),
    # Post
    path('post/<post_id>', views.post, name='post'),
    path('edit-post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('delete-post/<post_id>', views.delete_post, name='delete_post'),
    path('new-post/', views.new_post, name='new_post'),
    # User
    path('u/<user>', views.user, name='user'),
    path('follow/<user>', views.follow, name='follow'),
]
