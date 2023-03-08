from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('edit-profile/<int:pk>', views.EditProfile.as_view(), name='edit_profile'),
    path('settings/<int:pk>', views.UserSettings.as_view(), name='settings'),
]
