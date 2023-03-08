# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# My imports
from social.models import Post, Reply


# Moderation page
@login_required
def moderation(request):
    if request.user.is_staff:
        reported_posts = Post.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        reported_replies = Reply.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        return render(
            request,
            'moderation.html', {
                'reported_posts': reported_posts,
                'reported_replies': reported_replies,
                })
    else:
        return render(request, 'permission-error.html')


# Moderator delete post
@login_required
def mod_delete_post(request, post_id):    
    if request.user.is_staff:
        post = get_object_or_404(Post, id=post_id)
        post.user.mod_deleted += 1
        post.user.save()
        post.delete()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')


# Moderator delete reply
@login_required
def mod_delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if request.user.is_staff:
        reply.user.mod_deleted += 1
        reply.user.save()
        reply.delete()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')


# Post is okay
@login_required
def post_is_okay(request, post_id):
    if request.user.is_staff:
        post = get_object_or_404(Post, id=post_id)
        post.reported.clear()
        post.save()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')


# Reply is okay
@login_required
def reply_is_okay(request, reply_id):
    if request.user.is_staff:
        reply = get_object_or_404(Reply, id=reply_id)
        reply.reported.clear()
        reply.hidden = False
        reply.save()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')
