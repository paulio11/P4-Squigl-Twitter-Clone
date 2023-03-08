# Django imports
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# My imports
from .models import Post, Reply


# Home
def home(request):
    return render(request, 'home.html')


# Feed (followed user's and own posts)
def feed(request):
    following = request.user.following
    posts = Post.objects.filter(
        Q(user__in=following.all()) | Q(user=request.user))

    return render(request, 'feed.html', {
        'posts': posts,
    })


# Post
def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = Reply.objects.filter(post_id=post_id).order_by('date')

    return render(request, 'post.html', {
        'post': post,
        'replies': replies,
    })
