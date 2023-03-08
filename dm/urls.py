# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('send/<user_id>', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
]
