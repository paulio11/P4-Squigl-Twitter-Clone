# Django imports
from django.test import TestCase

# My imports
from .models import Message
from accounts.models import CustomUser

# Other imports
from model_bakery import baker


class MessageModelTests(TestCase):

    def setUp(self):
        self.testuser = baker.make(
            'accounts.CustomUser',
            username='sender'
        )
        self.testuser2 = baker.make(
            'accounts.CustomUser',
            username='recipient'
        )
        self.message = baker.make(
            'dm.Message',
            sender=self.testuser,
            recipient=self.testuser2,
        )

    def test_str(self):
        self.assertEqual(
            str(self.message), f'Message from: sender, to: recipient'
        )
