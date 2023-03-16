# Django imports
from django.test import TestCase, Client
from django.urls import resolve, reverse

# My imports
from .models import *
from accounts.models import CustomUser

# Other imports
from model_bakery import baker
from datetime import datetime, timedelta


class TestURLs(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply', post=self.post)

    def test_feed(self):
        resolver = resolve('/feed/')
        self.assertEqual(resolver.view_name, 'feed')

    def test_search(self):
        resolver = resolve('/search/')
        self.assertEqual(resolver.view_name, 'search')

    def test_post(self):
        resolver = resolve(f'/p/{self.post.id}')
        self.assertEqual(resolver.view_name, 'post')

    def test_edit_post(self):
        resolver = resolve(f'/edit-post/{self.post.id}')
        self.assertEqual(resolver.view_name, 'edit_post')

    def test_delete_post(self):
        resolver = resolve(f'/delete-post/{self.post.id}')
        self.assertEqual(resolver.view_name, 'delete_post')

    def test_like_post(self):
        resolver = resolve(f'/like-post/{self.post.id}')
        self.assertEqual(resolver.view_name, 'like_post')

    def test_repost_post(self):
        resolver = resolve(f'/repost/{self.post.id}')
        self.assertEqual(resolver.view_name, 'repost')

    def test_report_post(self):
        resolver = resolve(f'/report-post/{self.post.id}')
        self.assertEqual(resolver.view_name, 'report_post')

    def test_edit_reply(self):
        resolver = resolve(f'/edit-reply/{self.reply.id}')
        self.assertEqual(resolver.view_name, 'edit_reply')

    def test_delete_reply(self):
        resolver = resolve(f'/delete-reply/{self.reply.id}')
        self.assertEqual(resolver.view_name, 'delete_reply')

    def test_report_reply(self):
        resolver = resolve(f'/report-reply/{self.reply.id}')
        self.assertEqual(resolver.view_name, 'report_reply')

    def test_user(self):
        resolver = resolve(f'/u/{self.testuser}')
        self.assertEqual(resolver.view_name, 'user')

    def test_follow_user(self):
        resolver = resolve(f'/follow/{self.testuser}')
        self.assertEqual(resolver.view_name, 'follow')

    def test_mentions(self):
        resolver = resolve('/mentions/')
        self.assertEqual(resolver.view_name, 'mentions')

    def test_mark_read_mentions(self):
        resolver = resolve('/mentions/read/')
        self.assertEqual(resolver.view_name, 'mark_read')

    def test_trending_list(self):
        resolver = resolve('/trending/')
        self.assertEqual(resolver.view_name, 'trending')

    def test_user_list(self):
        resolver = resolve('/user-list/')
        self.assertEqual(resolver.view_name, 'user_list')


class TestReverseURLs(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply', post=self.post)

    def test_feed(self):
        url = reverse('feed')
        self.assertEqual(url, '/feed/')

    def test_search(self):
        url = reverse('search')
        self.assertEqual(url, '/search/')

    def test_post(self):
        url = reverse('post', args=[self.post.id])
        self.assertEqual(url, f'/p/{self.post.id}')

    def test_edit_post(self):
        url = reverse('edit_post', args=[self.post.id])
        self.assertEqual(url, f'/edit-post/{self.post.id}')

    def test_delete_post(self):
        url = reverse('delete_post', args=[self.post.id])
        self.assertEqual(url, f'/delete-post/{self.post.id}')

    def test_like_post(self):
        url = reverse('like_post', args=[self.post.id])
        self.assertEqual(url, f'/like-post/{self.post.id}')

    def test_repost_post(self):
        url = reverse('repost', args=[self.post.id])
        self.assertEqual(url, f'/repost/{self.post.id}')

    def test_report_post(self):
        url = reverse('report_post', args=[self.post.id])
        self.assertEqual(url, f'/report-post/{self.post.id}')

    def test_edit_reply(self):
        url = reverse('edit_reply', args=[self.reply.id])
        self.assertEqual(url, f'/edit-reply/{self.reply.id}')

    def test_delete_reply(self):
        url = reverse('delete_reply', args=[self.reply.id])
        self.assertEqual(url, f'/delete-reply/{self.reply.id}')

    def test_report_reply(self):
        url = reverse('report_reply', args=[self.reply.id])
        self.assertEqual(url, f'/report-reply/{self.reply.id}')

    def test_user(self):
        url = reverse('user', args=[self.testuser])
        self.assertEqual(url, f'/u/{self.testuser}')

    def test_follow_user(self):
        url = reverse('follow', args=[self.testuser])
        self.assertEqual(url, f'/follow/{self.testuser}')

    def test_mentions(self):
        url = reverse('mentions')
        self.assertEqual(url, '/mentions/')

    def test_mark_read_mentions(self):
        url = reverse('mark_read')
        self.assertEqual(url, '/mentions/read/')

    def test_trending_list(self):
        url = reverse('trending')
        self.assertEqual(url, '/trending/')

    def test_user_list(self):
        url = reverse('user_list')
        self.assertEqual(url, '/user-list/')


class TestPostModel(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.testuser2 = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')

    def test_str(self):
        self.assertEqual(
            str(self.post), f'Post: {self.post.id}, by: {self.post.user}'
        )

    def test_post_has_user(self):
        self.assertIsNotNone(self.post.user)

    def test_post_has_date(self):
        self.assertIsNotNone(self.post.date)

    def test_post_has_post(self):
        self.assertIsNotNone(self.post.post)

    def test_like_count(self):
        self.post.likes.set([self.testuser, self.testuser2])
        self.assertEqual(self.post.likes.count(), 2)

    def test_reply_count(self):
        reply1 = baker.make('social.Reply', post=self.post)
        reply2 = baker.make('social.Reply', post=self.post)
        self.assertEqual(self.post.reply.count(), 2)

    def test_repost(self):
        self.repost = baker.make('social.Post', repost_post=self.post)
        self.assertEqual(self.repost.repost_post, self.post)

    def test_read(self):
        self.post.read.set([self.testuser, self.testuser2])
        self.assertEqual(self.post.read.count(), 2)

    def test_report(self):
        self.post.reported.set([self.testuser, self.testuser2])
        self.assertEqual(self.post.reported.count(), 2)

    def test_post_length(self):
        self.assertLessEqual(len(self.post.post), 400)

    def test_link_length(self):
        self.assertLessEqual(len(self.post.link), 50)

    # def test_time_check(self):
    #     yesterday = datetime.now() - timedelta(hours=24)
    #     self.oldpost = baker.make('social.Post', date=yesterday)
    #     self.assertFalse(self.oldpost.time_check())


class TestReplyModel(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.testuser2 = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make(
            'social.Reply',
            user=self.testuser,
            post=self.post
        )

    def test_str(self):
        self.assertEqual(
            str(self.reply),
            f'Reply: {self.reply.id}, for: {self.post}, by: {self.testuser}'
        )

    def test_reply_has_user(self):
        self.assertIsNotNone(self.reply.user)

    def test_reply_has_date(self):
        self.assertIsNotNone(self.reply.date)

    def test_reply_has_reply(self):
        self.assertIsNotNone(self.reply.reply)

    def test_reply_not_hidden(self):
        self.assertFalse(self.reply.hidden)

    def test_reply_report(self):
        self.reply.reported.set([self.testuser, self.testuser2])
        self.assertEqual(self.reply.reported.count(), 2)

    def test_reply_read(self):
        self.reply.read.set([self.testuser, self.testuser2])
        self.assertEqual(self.reply.read.count(), 2)

    def test_reply_length(self):
        self.assertLessEqual(len(self.reply.reply), 400)


class TestLoginRequiredViews(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')
        self.user.set_password('1234')
        self.user.save()
        self.user2 = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply')
        self.c = Client()

    def test_feed(self):
        response = self.c.get('/feed/')
        self.assertEqual(response.status_code, 302)

    def test_feed_logged_in(self):
        self.c.login(username='testuser', password='1234')
        response = self.c.get('/feed/')
        self.assertEqual(response.status_code, 200)

    def test_new_post(self):
        response = self.c.get('/new-post/')
        self.assertEqual(response.status_code, 302)

    def test_new_post_logged_in(self):
        self.c.login(username='testuser', password='1234')
        response = self.c.get('/new-post/')
        self.assertEqual(response.status_code, 200)

    def test_repost(self):
        response = self.c.get(f'/repost/{self.post.id}')
        self.assertEqual(response.status_code, 302)

    def test_repost_logged_in(self):
        self.c.login(username='testuser', password='1234')
        response = self.c.get(f'/repost/{self.post.id}')
        self.assertEqual(response.status_code, 200)

    def test_report_post(self):
        response = self.c.get(f'/report-post/{self.post.id}')
        self.assertEqual(response.status_code, 302)

    # def test_report_reply(self):
    #     response = self.c.get(f'/report-reply/{self.reply.id}')
    #     self.assertEqual(response.status_code, 302)

    # Testing csrf token forms?

    def test_follow_user(self):
        response = self.c.get(f'/follow/{self.user2}')
        self.assertEqual(response.status_code, 302)

    # def test_follow_user_logged_in(self):
    #     self.c.login(username='testuser', password='1234')
    #     response = self.c.get(f'/follow/{self.user2}')
    #     self.assertEqual(response.status_code, 200)

    def test_mentions(self):
        response = self.c.get('/mentions/')
        self.assertEqual(response.status_code, 302)

    def test_mentions_logged_in(self):
        self.c.login(username='testuser', password='1234')
        response = self.c.get('/mentions/')
        self.assertEqual(response.status_code, 200)

    def test_mark_read(self):
        response = self.c.get('/mentions/read/')
        self.assertEqual(response.status_code, 302)

    def test_mark_read_logged_in(self):
        self.c.login(username='testuser', password='1234')
        response = self.c.get('/mentions/read/')
        self.assertEqual(response.status_code, 302)