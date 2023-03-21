# Django imports
from django.test import TestCase

# My imports
from .templatetags.moderation_extras import mod_count

# Other imports
from model_bakery import baker


# Template tag tests

class ModCountTests(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.testuser2 = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply')
        self.message = baker.make('dm.Message', reported=True)
        self.post.reported.set([self.testuser])
        self.reply.reported.set([self.testuser])

    def test_mod_count(self):
        self.assertEqual(mod_count(), 3)
