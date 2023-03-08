from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Feed
    path('feed/', views.feed, name='feed'),
    # Search
    path('search/', views.search, name='search'),
    # Post
    path('post/<post_id>', views.post, name='post'),
    path('edit-post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('delete-post/<post_id>', views.delete_post, name='delete_post'),
    path('new-post/', views.new_post, name='new_post'),
    path('like-post/<post_id>', views.like_post, name='like_post'),
    path('repost/<post_id>', views.repost, name='repost'),
    # Reply
    path('edit-reply/<int:pk>', views.EditReply.as_view(), name='edit_reply'),
    path('delete-reply/<reply_id>', views.delete_reply, name='delete_reply'),
    path('hide-reply/<reply_id>', views.hide_reply, name='hide_reply'),
    # User
    path('u/<user>', views.user, name='user'),
    path('follow/<user>', views.follow, name='follow'),
    # Mentions
    path('mentions/', views.mentions, name='mentions'),
]
