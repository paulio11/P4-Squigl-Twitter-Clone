# Django imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('social.urls')),
    path('mod/', include('moderation.urls')),
    path('admin/', admin.site.urls),
    path('messages/', dm.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
