# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# My imports
from social.models import Post


# Moderation page
@login_required
def moderation(request):
    if request.user.is_staff:
        reported_posts = Post.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        return render(
            request,
            'moderation.html',
            {'reported_posts': reported_posts})
    else:
        return render(request, 'permission-error.html')


# Moderator delete post
@login_required
def mod_delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_staff:
        post.user.deleted_posts += 1
        post.user.save()
        post.delete()
        return redirect('moderation')
    else:
        return render(request, 'permission-error.html')
