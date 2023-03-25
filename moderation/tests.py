# Django imports
from django.test import TestCase, Client
from django.urls import reverse

# My imports
from .templatetags.moderation_extras import mod_count
from social.models import Post, Reply
from dm.models import Message
from accounts.models import CustomUser

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


# Views tests

class ModerationTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.client = Client()
        self.url = reverse('moderation')

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'Only Squigl moderators can')

    def test_moderation(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderation/moderation.html')


class ModDeletePostTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.post = baker.make('social.Post')
        self.client = Client()
        self.url = reverse('mod_delete_post', args={self.post.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this')

    def test_mod_delete(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.post.user.refresh_from_db()
        self.assertEquals(Post.objects.count(), 0)
        self.assertEquals(self.post.user.strikes, 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')


class ModDeleteReplyTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply')
        self.client = Client()
        self.url = reverse('mod_delete_reply', args={self.reply.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this')

    def test_mod_delete(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.reply.user.refresh_from_db()
        self.assertEquals(Reply.objects.count(), 0)
        self.assertEquals(self.reply.user.strikes, 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')


class ModDeleteMessageTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.message = baker.make('dm.Message')
        self.client = Client()
        self.url = reverse('mod_delete_msg', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this')

    def test_mod_delete(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.message.sender.refresh_from_db()
        self.assertEquals(Message.objects.count(), 0)
        self.assertEquals(self.message.sender.strikes, 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')


class PostIsOkayTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.post = baker.make('social.Post')
        self.post.reported.set([self.testuser])
        self.client = Client()
        self.url = reverse('mod_post_okay', args={self.post.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not okay this post')

    def test_post_okay(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')
        self.assertEqual(self.post.reported.count(), 0)


class ReplyIsOkayTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.post = baker.make('social.Post')
        self.reply = baker.make('social.Reply')
        self.reply.reported.set([self.testuser])
        self.client = Client()
        self.url = reverse('mod_reply_okay', args={self.reply.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not okay this reply')

    def test_reply_okay(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.reply.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')
        self.assertEqual(self.reply.reported.count(), 0)


class MessageIsOkayTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.message = baker.make('dm.Message', reported=True)
        self.client = Client()
        self.url = reverse('mod_msg_okay', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not okay this message')

    def test_message_okay(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.message.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')
        self.assertFalse(self.message.reported)


class BanUserTests(TestCase):

    def setUp(self):
        self.testmod = CustomUser.objects.create_user(
            username='testmod',
            password='testpass',
            email='1@1.com',
            is_staff=True,
        )
        self.testuser = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            email='1@2.com',
            is_staff=False,
        )
        self.client = Client()
        self.url = reverse('ban_user', args={self.testuser.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_login_as_normal_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not ban this user')

    def test_ban_user(self):
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.testuser.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')
        self.assertFalse(self.testuser.is_active)

    def test_unban_user(self):
        self.testuser.is_active = False
        self.testuser.save()
        self.client.login(username='testmod', password='testpass')
        response = self.client.get(self.url)
        self.testuser.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mod/')
        self.assertTrue(self.testuser.is_active)