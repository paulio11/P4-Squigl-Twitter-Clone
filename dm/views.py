# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# My imports
from .models import Message
from .forms import MessageForm
from accounts.models import CustomUser


# Message inbox
@login_required
def messages(request):
    unread_messages = Message.objects.filter(
        recipient=request.user).filter(read=False).order_by('-date')
    messages = Message.objects.filter(
        recipient=request.user).filter(read=True).order_by('-date')
    sent_messages = Message.objects.filter(
        sender=request.user).order_by('-date')
    return render(request, 'dm/messages.html', {
        'unread_messages': unread_messages,
        'messages': messages,
        'sent_messages': sent_messages})


# Send user message
@login_required
def send_message(request, user_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = get_object_or_404(CustomUser, id=user_id)
            message.save()
            return redirect('user', message.recipient)
    else:
        return render(request, 'dm/send-message.html', {'form': MessageForm()})
