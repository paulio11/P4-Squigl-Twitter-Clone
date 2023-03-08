# Django imports
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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
    users = CustomUser.objects.exclude(
        id__in=following.all()).exclude(id=request.user.id).order_by('?')[:5]

    return render(request, 'feed.html', {
        'posts': posts,
        'users': users,
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
def user(request, user):
    queryset = CustomUser.objects
    user = get_object_or_404(queryset, username=user)
    posts = Post.objects.filter(user_id=user.id).order_by('-date')
    following = False

    if request.user.is_authenticated:
        if request.user.following.filter(id=user.id):
            following = True

    return render(request, 'user.html', {
        'user': user,
        'posts': posts,
        'following': following,
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


# Edit post
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit-post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={
            'post_id': self.object.id,
        })


# Delete post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        post.delete()
        return redirect('feed')
    else:
        return render(request, 'delete-error.html')


# Like Post
def like_post(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponse('Success!')


# Follow user
def follow(request, user):
    user = get_object_or_404(CustomUser, username=user)
    followed = request.user.following.filter(username=user).exists()

    if followed:
        request.user.following.remove(user)
    else:
        request.user.following.add(user)

    return redirect('user', user)
