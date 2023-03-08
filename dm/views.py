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
        recipient=request.user).filter(read=True).exclude(
            recipient_del=True).order_by('-date')
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


# Send reply
@login_required
def send_reply(request, message_id):
    old_msg = get_object_or_404(Message, id=message_id)
    if old_msg.recipient == request.user:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                old_msg.read = True
                message = form.save(commit=False)
                message.sender = old_msg.recipient
                message.recipient = old_msg.sender
                message.save()
                return redirect('messages')
        else:
            return render(request, 'dm/send-message.html', {
                'form': MessageForm()})
    else:
        return render(request, 'permission-error.html')


# Mark message read
@login_required
def mark_read(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.recipient == request.user:
        message.read = True
        message.save()
        return redirect('messages')
    else:
        return render(request, 'permission-error.html')


# Delete message
@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.sender:
        message.sender_del = True
        message.save()
    elif request.user == message.recipient:
        message.read = True
        message.recipient_del = True
        message.save()
    else:
        return render(request, 'permission-error.html')
    if message.recipient_del and message.sender_del:
        message.delete()
    return redirect('messages')



# Report
# Mark read

