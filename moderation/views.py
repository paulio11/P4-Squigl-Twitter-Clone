# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# My imports
from social.models import Post, Reply
from dm.models import Message


# Moderation page
@login_required
def moderation(request):
    if request.user.is_staff:
        reported_posts = Post.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        reported_replies = Reply.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        reported_messages = Message.objects.filter(reported=True)
        return render(
            request,
            'moderation.html', {
                'reported_posts': reported_posts,
                'reported_replies': reported_replies,
                'reported_messages': reported_messages,
                })
    else:
        return render(request, 'permission-error.html')


# Moderator delete post
@login_required
def mod_delete_post(request, post_id):    
    if request.user.is_staff:
        post = get_object_or_404(Post, id=post_id)
        post.user.strikes += 1
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
        reply.user.strikes += 1
        reply.user.save()
        reply.delete()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')


# Moderator delete message
@login_required
def mod_delete_msg(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user.is_staff:
        message.sender.strikes += 1
        message.sender.save()
        message.delete()
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


# Message is okay
@login_required
def msg_is_okay(request, message_id):
    if request.user.is_staff:
        message = get_object_or_404(Message, id=message_id)
        message.reported = False
        message.save()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')
