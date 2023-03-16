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
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        return redirect('login')


# Feed (followed user's and own posts)
@login_required
def feed(request):
    following = request.user.following
    posts = Post.objects.filter(
        Q(user__in=following.all()) | Q(user=request.user))

    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'social/feed.html', {
        'post_count': posts.count(),
        'page_obj': page_obj,
    })


# Search
def search(request):
    if request.method == 'POST':
        query = request.POST['query'].strip().lower()
        users = CustomUser.objects.filter(
            Q(username__icontains=query) | Q(name__icontains=query)).order_by(
                'username')
        posts = Post.objects.filter(
            post__icontains=query).order_by('-date')
        replies = Reply.objects.filter(
            reply__icontains=query).exclude(hidden=True).order_by('-date')
        return render(request, 'social/search.html', {
            'query': query,
            'posts': posts,
            'users': users,
            'replies': replies,
        })
    else:
        return render(request, 'social/search.html')


# Post
def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = Reply.objects.filter(post_id=post_id).order_by('-date')

    if request.method == 'POST':
        form1 = ReplyForm(data=request.POST, prefix='f1')
        if form1.is_valid():
            form1.instance.user = request.user
            form1.instance.post = post
            form1.save()
            return HttpResponseRedirect(request.path_info)
        form2 = ReplyForm(data=request.POST, prefix='f2')
        if form2.is_valid():
            form2.instance.user = request.user
            form2.instance.post = post
            form2.save()
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'social/post.html', {
            'post': post,
            'replies': replies,
            'form1': ReplyForm(prefix='f1'),
            'form2': ReplyForm(prefix='f2'),
        })


# User
def user(request, user):
    queryset = CustomUser.objects
    user = get_object_or_404(queryset, username=user)
    posts = Post.objects.filter(user_id=user.id).order_by('-date')
    following = False

    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        if request.user.following.filter(id=user.id):
            following = True

    return render(request, 'social/user.html', {
        'user': user,
        'page_obj': page_obj,
        'post_count': posts.count(),
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
        return render(request, 'new/new-post.html', {'form': PostForm()})


# Repost
@login_required
def repost(request, post_id):
    old_post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.repost_post = old_post
            post.save()
            return redirect('post', post.id)
    else:
        return render(
            request, 'new/new-repost.html', {
                'form': PostForm(), 'post': old_post})


# Edit post
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit/edit-post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={
            'post_id': self.object.id,
        })


# Edit reply
class EditReply(UpdateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'edit/edit-reply.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={
            'post_id': self.object.post.id,
        })


# Delete post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        post.delete()
        return redirect('feed')
    else:
        e = 'You can not delete this post because you are not the author.'
        return render(request, 'error.html', {'e': e})


# Delete reply
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if request.user == reply.user:
        reply.delete()
        return redirect('post', reply.post.id)
    else:
        e = 'You can not delete this reply because you are not the author.'
        return render(request, 'error.html', {'e': e})


# Like post
def like_post(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponse('Success!')


# Report post
@login_required
def report_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.reported.add(request.user)
    post.save()
    return redirect('post', post.id)


# Hide reply
def report_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if request.user == reply.post.user:
        reply.hidden = True
    reply.reported.add(request.user)
    reply.save()
    return redirect('post', reply.post.id)


# Follow user
@login_required
def follow(request, user):
    user = get_object_or_404(CustomUser, username=user)
    followed = request.user.following.filter(username=user).exists()

    if followed:
        request.user.following.remove(user)
    else:
        request.user.following.add(user)

    return redirect(request.META['HTTP_REFERER'])


# Mentions
@login_required
def mentions(request):
    posts = Post.objects.filter(post__icontains=request.user).exclude(
        read=request.user).order_by('-date')
    replies = Reply.objects.filter(reply__icontains=request.user).exclude(
        hidden=True).exclude(read=request.user).order_by('-date')
    return render(request, 'social/mentions.html', {
        'posts': posts,
        'replies': replies,
    })


# Mark mentions as read
@login_required
def mark_read(request):
    posts = Post.objects.filter(post__icontains=request.user).exclude(
        read=request.user)
    replies = Reply.objects.filter(reply__icontains=request.user).exclude(
        hidden=True).exclude(read=request.user)
    for post in posts:
        post.read.add(request.user)
    for reply in replies:
        reply.read.add(request.user)
    return redirect('mentions')


# Trending hashtags
def trending(request):
    return render(request, 'social/hashtags.html')


# User list
def user_list(request):
    return render(request, 'social/user-list.html')
