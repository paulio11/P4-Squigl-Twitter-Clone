# Django imports
from django.urls import path

# My imports
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        'edit-profile/<int:pk>',
        views.EditProfile.as_view(),
        name='edit_profile'),
    path('settings/<int:pk>', views.UserSettings.as_view(), name='settings'),
    path('password/', views.change_password, name='password'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
