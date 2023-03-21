# Django imports
from django.test import TestCase
from django.utils.timezone import make_aware

# My imports
from social.models import Post, Reply

# Other imports
from model_bakery import baker
from datetime import datetime, timedelta


# Model tests

class PostModelTests(TestCase):

    def setUp(self):
        self.user = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')

    def test_str(self):
        self.assertEqual(
            str(self.post), f'Post: {self.post.id}, by: {self.post.user}'
        )

    def test_like_count(self):
        self.post.likes.set([self.user])
        self.assertEqual(self.post.like_count(), 1)

    def test_reply_count(self):
        reply = baker.make('social.Reply', post=self.post)
        self.assertEqual(self.post.reply_count(), 1)

    def test_repost_count(self):
        repost = baker.make('social.Post', repost_post=self.post)
        self.assertEqual(self.post.repost_count(), 1)

    def test_reported_count(self):
        self.post.reported.set([self.user])
        self.assertEqual(self.post.reported_count(), 1)

    def test_time_check(self):
        self.assertTrue(self.post.time_check())

    def test_time_check_2(self):
        now = datetime.now()
        more_than_24h_ago = now - timedelta(hours=25)
        aware_datetime = make_aware(more_than_24h_ago)
        self.post.date = aware_datetime
        self.post.save()
        self.assertFalse(self.post.time_check())


class ReplyModelTests(TestCase):

    def setUp(self):
        self.user = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply')

    def test_str(self):
        self.assertEqual(
            str(self.reply), f'Reply: {self.reply.id}, for: {self.reply.post}, by: {self.reply.user}'
        )

    def test_reported_count(self):
        self.reply.reported.set([self.user])
        self.assertEqual(self.reply.reported_count(), 1)

    def test_time_check(self):
        self.assertTrue(self.reply.time_check())

    def test_time_check_2(self):
        now = datetime.now()
        more_than_24h_ago = now - timedelta(hours=25)
        aware_datetime = make_aware(more_than_24h_ago)
        self.reply.date = aware_datetime
        self.reply.save()
        self.assertFalse(self.reply.time_check())