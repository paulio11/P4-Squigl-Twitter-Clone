# Django imports
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# My imports
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from accounts.models import CustomUser


# Home
def home(request):
    return render(request, 'home.html')


# Feed (followed user's and own posts)
@login_required
def feed(request):
    following = request.user.following
    posts = Post.objects.filter(
        Q(user__in=following.all()) | Q(user=request.user))
    users = CustomUser.objects.exclude(
        id__in=following.all()).exclude(id=request.user.id).order_by('?')[:10]
    recent_hashtags = Post.objects.filter(
        post__contains='#')[:100]

    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        'users': users,
        'recent_hashtags': recent_hashtags,
        'page_obj': page_obj,
    })


# Search
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        users = CustomUser.objects.filter(
            username__icontains=query).order_by('username')
        posts = Post.objects.filter(
            post__icontains=query).order_by('-date')
        return render(request, 'search.html', {
            'query': query,
            'posts': posts,
            'users': users,
        })
    else:
        return render(request, 'search.html')


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
def user(request, user):
    queryset = CustomUser.objects
    user = get_object_or_404(queryset, username=user)
    posts = Post.objects.filter(user_id=user.id).order_by('-date')
    # liked_posts = user.post_likes.all()
    following = False

    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        if request.user.following.filter(id=user.id):
            following = True

    return render(request, 'user.html', {
        'user': user,
        'page_obj': page_obj,
        'post_count': posts.count(),
        # 'liked_posts': liked_posts,
        'following': following,
    })


# New post
@login_required
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


# Repost
@login_required
def repost(request, post_id):
    old_post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            old_post.reposter.add(request.user)
            post.user = request.user
            post.repost_post = old_post
            post.save()
            return redirect('post', post.id)
    else:
        return render(
            request, 'new-repost.html', {
                'form': PostForm(), 'post': old_post})


# Edit post
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit-post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={
            'post_id': self.object.id,
        })


# Edit reply
class EditReply(UpdateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'edit-reply.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={
            'post_id': self.object.post.id,
        })


# Delete post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        if post.repost_post.reposter.filter(id=request.user.id).exists():
            post.repost_post.reposter.remove(request.user)
        post.delete()
        return redirect('feed')
    else:
        return render(request, 'permission-error.html')


# Delete reply
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if request.user == reply.user:
        reply.delete()
        return redirect('post', reply.post.id)
    else:
        return render(request, 'permission-error.html')


# Hide reply
def hide_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if request.user == reply.post.user:
        reply.hidden = True
        reply.save()
        return redirect('post', reply.post.id)
    else:
        return render(request, 'permission_error.html')


# Like post
def like_post(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponse('Success!')


# Follow user
@login_required
def follow(request, user):
    user = get_object_or_404(CustomUser, username=user)
    followed = request.user.following.filter(username=user).exists()

    if followed:
        request.user.following.remove(user)
    else:
        request.user.following.add(user)

    return redirect('user', user)
