# Django imports
from django.test import TestCase, Client
from django.urls import reverse
from django.utils.timezone import make_aware

# My imports
from social.models import Post, Reply
from social.forms import ReplyForm, PostForm
from accounts.models import CustomUser
from .templatetags.social_extras import user_has_replied, upto

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
            str(self.reply), (
                f'Reply: {self.reply.id}, for: {self.reply.post},'
                f' by: {self.reply.user}')
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


# Template tag tests

class UserHasRepliedTagTests(TestCase):

    def setUp(self):
        self.user = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post')
        self.reply = Reply.objects.create(
            post=self.post,
            user=self.user,
            reply='test reply'
        )

    def test_replies_gte_1(self):
        self.assertTrue(user_has_replied(self.user, self.post))

    def test_replies_0(self):
        self.reply.delete()
        self.assertFalse(user_has_replied(self.user, self.post))


class StringFilterTests(TestCase):

    def test_upto(self):
        string = '2 hours, 55 minutes'
        self.assertEquals(upto(string, ','), '2 hours')


# View tests

class HomeTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = Client()
        self.url = reverse('home')

    def test_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/feed/')

    def test_logged_out(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


class FeedTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = Client()
        self.url = reverse('feed')

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_render(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/feed.html')


class SearchTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('search')

    def test_post(self):
        response = self.client.post(self.url, {
            'query': 'test query'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/search.html')
        self.assertContains(response, 'test query')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/search.html')


class PostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post', user=self.user)
        self.reply = baker.make('social.Reply', post=self.post)
        self.client = Client()
        self.url = reverse('post', args=[self.post.id])

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('social/post.html')
        self.assertIsInstance(response.context['form1'], ReplyForm)
        self.assertIsInstance(response.context['form2'], ReplyForm)
        self.assertContains(response, self.post.post)
        self.assertContains(response, self.reply.reply)
        self.assertContains(response, 'if you want to reply to this post.')

    def test_post_reply_form_1(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'f1-reply': 'test reply',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reply.objects.count(), 2)
        self.assertTemplateUsed('social/post.html')
        self.assertContains(response, self.post.post)
        self.assertContains(response, self.reply.reply)
        self.assertContains(response, 'test reply')

    def test_post_reply_form_2(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'f2-reply': 'test reply',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reply.objects.count(), 2)
        self.assertTemplateUsed('social/post.html')
        self.assertContains(response, self.post.post)
        self.assertContains(response, self.reply.reply)
        self.assertContains(response, 'test reply')


class UserTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.user2 = baker.make('accounts.CustomUser')
        self.post = baker.make('social.Post', user=self.user2)
        self.client = Client()
        self.url = reverse('user', args=[self.user2])

    def test_render(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed('social/user.html')
        self.assertContains(response, self.post.post)

    def test_when_following(self):
        self.user.following.set([self.user2])
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertContains(response, 'Following')

    def test_when_not_following(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertContains(response, 'Follow')


class NewPostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = Client()
        self.url = reverse('new_post')

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('new/new-post.html')
        self.assertIsInstance(response.context['form'], PostForm)

    def test_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'post': 'test post',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post', args='1'))
        self.assertTemplateUsed('social/post.html')
        self.assertEqual(Post.objects.count(), 1)


class RepostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.oldpost = baker.make('social.Post')
        self.client = Client()
        self.url = reverse('repost', args=[self.oldpost.id])

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('new/new-post.html')
        self.assertIsInstance(response.context['form'], PostForm)
        self.assertContains(response, self.oldpost.post)

    def test_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'post': 'test repost',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post', args='2'))
        self.assertTemplateUsed('social/post.html')
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(self.oldpost.repost_count(), 1)


class EditPostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post', user=self.user)
        self.client = Client()
        self.url = reverse('edit_post', kwargs={'pk': self.post.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit/edit-post.html')
        self.assertContains(response, 'You do not have permission')

    def test_get_as_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit/edit-post.html')
        self.assertContains(response, self.post.post)

    def test_post(self):
        data = {'post': 'edited post'}
        response = self.client.post(self.url, data=data)
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.post, 'edited post')
        self.assertRedirects(response, f'/p/{self.post.id}')


class EditReplyTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply', user=self.user)
        self.client = Client()
        self.url = reverse('edit_reply', kwargs={'pk': self.reply.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit/edit-reply.html')
        self.assertContains(response, 'You do not have permission')

    def test_get_as_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit/edit-reply.html')
        self.assertContains(response, self.reply.reply)

    def test_post(self):
        data = {'reply': 'edited reply'}
        response = self.client.post(self.url, data=data)
        self.reply.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.reply.reply, 'edited reply')
        self.assertRedirects(response, f'/p/{self.reply.post.id}')


class DeletePostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post', user=self.user)
        self.client = Client()
        self.url = reverse('delete_post', args={self.post.id})

    def test_delete(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this post')

    def test_delete_as_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('feed'))
        self.assertEquals(Post.objects.count(), 0)


class DeleteReplyTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.reply = baker.make('social.Reply', user=self.user)
        self.client = Client()
        self.url = reverse('delete_reply', args={self.reply.id})

    def test_delete(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this reply')

    def test_delete_as_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/p/{self.reply.post.id}')
        self.assertEquals(Reply.objects.count(), 0)


class LikePostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post')
        self.client = Client()
        self.url = reverse('like_post', args={self.post.pk})
        self.client.login(username='testuser', password='testpass')

    def test_like(self):
        response = self.client.get(self.url)
        self.assertEquals(self.post.likes.count(), 1)

    def test_unlike(self):
        self.post.likes.set([self.user])
        response = self.client.get(self.url)
        self.assertEquals(self.post.likes.count(), 0)


class ReportPostTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post')
        self.client = Client()
        self.url = reverse('report_post', args={self.post.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_report(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.post.refresh_from_db()
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('post', args={self.post.id}))
        self.assertEquals(self.post.reported_count(), 1)


class ReportReplyTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post', user=self.user)
        self.reply = baker.make('social.Reply', post=self.post)
        self.client = Client()
        self.url = reverse('report_reply', args={self.reply.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_report(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.reply.refresh_from_db()
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'post',
            args={self.reply.post.id}))
        self.assertEquals(self.reply.reported_count(), 1)
        self.assertTrue(self.reply.hidden)


class FollowTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.user2 = baker.make('accounts.CustomUser')
        self.client = Client()
        self.url = reverse('follow', args={self.user2})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_follow(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.user.refresh_from_db()
        self.user2.refresh_from_db()
        self.assertEquals(self.user.following_count(), 1)
        self.assertEquals(self.user2.followers_count(), 1)
        self.assertRedirects(response, reverse('user', args={self.user2}))

    def test_unfollow(self):
        self.user.following.set([self.user2])
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.user.refresh_from_db()
        self.user2.refresh_from_db()
        self.assertEquals(self.user.following_count(), 0)
        self.assertEquals(self.user2.followers_count(), 0)
        self.assertRedirects(response, reverse('user', args={self.user2}))


class MentionsTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = Client()
        self.url = reverse('mentions')

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_render(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/mentions.html')


class MarkReadTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )
        self.post = baker.make('social.Post', post=f'hello {self.user}')
        self.reply = baker.make('social.Reply', reply=f'hello {self.user}')
        self.client = Client()
        self.url = reverse('mark_read')

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_mark_read(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('mentions'))
        self.post.refresh_from_db()
        self.reply.refresh_from_db()
        self.assertEquals(self.post.read.count(), 1)
        self.assertEquals(self.reply.read.count(), 1)


class SideTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass'
        )

    def test_trending(self):
        response = self.client.get(reverse('trending'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/hashtags.html')

    def test_user_list(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('user_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('social/user_list.html')

    def test_ulist_login_required(self):
        response = self.client.get(reverse('user_list'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')
