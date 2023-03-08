# Django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

# My imports
from .models import Post, Reply
from .forms import ReplyForm
from accounts.models import CustomUser


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

    if request.method == 'POST':
        form = ReplyForm()
        form.instance.user = request.user
        form.instance.post = post
        form.save()
        return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'post.html', {
            'post': post,
            'replies': replies,
            'form': ReplyForm(),
        })


# User
def user(request, user_username):
    queryset = CustomUser.objects
    user = get_object_or_404(queryset, username=user_username)
    posts = Post.objects.filter(user_id=user.id).order_by('-date')

    return render(request, 'user.html', {
        'user': user,
        'posts': posts,
    })
