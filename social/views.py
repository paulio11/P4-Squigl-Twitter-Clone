# Django imports
from django.shortcuts import render
from django.db.models import Q

# My imports
from .models import Post


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
