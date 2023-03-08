# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('send/', views.send_message, name='send_message'),
]
