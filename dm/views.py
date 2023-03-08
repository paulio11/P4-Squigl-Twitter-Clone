# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# My imports
from .forms import MessageForm
from accounts.models import CustomUser


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
