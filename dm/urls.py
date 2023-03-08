# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('', views.messages, name='messages'),
    path('send/<user_id>', views.send_message, name='send_message'),
    path('reply/<message_id>', views.send_reply, name='send_reply'),
    path('read/<message_id>', views.mark_read, name='mark_read'),
    path('delete/<message_id>', views.delete_message, name='delete_message'),
    path('report/<message_id>', views.report_message, name='report_message')
]
