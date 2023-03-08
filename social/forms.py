# Django imports
from django.forms import ModelForm

# My imports
from .models import Reply


# Reply form
class ReplyForm(ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']
