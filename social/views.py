# Django imports
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

# My imports
from .models import Post, Reply
from .forms import PostForm, ReplyForm
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
    replies = Reply.objects.filter(post_id=post_id).order_by('-date')

    if request.method == 'POST':
        form = ReplyForm(data=request.POST)
        if form.is_valid():
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


# New post
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post', post.id)
    else:
        return render(request, 'new-post.html', {'form': PostForm()})
