# Django imports
from django.contrib import admin

# My imports
from .models import *


admin.site.register(Post)
admin.site.register(Reply)
