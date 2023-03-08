# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('', views.messages, name='messages'),
    path('send/<user_id>', views.send_message, name='send_message'),    
    path('read/<message_id>', views.mark_read, name='mark_read'),
]
