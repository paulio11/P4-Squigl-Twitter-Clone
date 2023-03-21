# Django imports
from django.test import TestCase, Client
from django.urls import reverse

# My imports
from .models import Message
from accounts.models import CustomUser

# Other imports
from model_bakery import baker


# Model Tests

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
            recipient=self.testuser2
        )

    def test_str(self):
        self.assertEqual(
            str(self.message), f'Message from: sender, to: recipient'
        )


# View Tests

class MessagesTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass')
        self.client = Client()
        self.url = reverse('messages')

    def test_login_requried(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_render(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('dm/messages.html')


class SendMessageTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass')
        self.testuser2 = baker.make('accounts.CustomUser')
        self.client = Client()
        self.url = reverse('send_message', args={self.testuser2.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'message': 'test message',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/u/{self.testuser2}')
        self.assertEqual(Message.objects.count(), 1)

    def test_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dm/send-message.html')
        self.assertContains(response, f'Send  Message to ~{self.testuser2}')


class SendReplyTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass', email='1@1.com')
        self.testuser2 = CustomUser.objects.create_user(
            username='testuser2', password='testpass', email='1@2.com')
        self.message = Message.objects.create(
            sender=self.testuser2,
            recipient=self.testuser,
        )
        self.client = Client()
        self.url = reverse('send_reply', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {
            'message': 'test message',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/messages/')
        self.assertEqual(Message.objects.count(), 2)

    def test_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dm/send-message.html')
        self.assertContains(response, f'Send Reply to ~testuser2')

    def test_error(self):
        self.client.login(username='testuser2', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not reply to this message because you are not the recipient.')


class MarkReadTests(TestCase):

    def setUp(self):
        self.recipient = CustomUser.objects.create_user(
            username='recipient', password='testpass', email='1@1.com')
        self.sender = baker.make('accounts.CustomUser')
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass', email='1@3.com')
        self.message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            message='test message'
        )
        self.client = Client()
        self.url = reverse('mark_read', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_mark_read(self):
        self.client.login(username='recipient', password='testpass')
        response = self.client.get(self.url)
        self.message.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/messages/')
        self.assertTrue(self.message.read)

    def test_error(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not mark this message as read because you are not the recipient.')


class DeleteMessageTests(TestCase):

    def setUp(self):
        self.sender = CustomUser.objects.create_user(
            username='sender', password='testpass', email='1@1.com')
        self.recipient = CustomUser.objects.create_user(
            username='recipient', password='testpass', email='1@2.com')
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass', email='1@3.com')
        self.message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            message='test message'
        )
        self.client = Client()
        self.url = reverse('delete_message', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_sender_delete(self):
        self.client.login(username='sender', password='testpass')
        response = self.client.get(self.url)
        self.message.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/messages/')
        self.assertTrue(self.message.sender_del)

    def test_recipient_delete(self):
        self.client.login(username='recipient', password='testpass')
        response = self.client.get(self.url)
        self.message.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/messages/')
        self.assertTrue(self.message.recipient_del)

    def test_delete(self):
        self.message.sender_del = True
        self.message.save()
        self.client.login(username='recipient', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(Message.objects.count(), 0)

    def test_error(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not delete this message because you are neither the recipient or sender.')


class ReportMessageTests(TestCase):

    def setUp(self):
        self.recipient = CustomUser.objects.create_user(
            username='recipient', password='testpass', email='1@1.com')
        self.sender = baker.make('accounts.CustomUser')
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass', email='1@3.com')
        self.message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            message='test message'
        )
        self.client = Client()
        self.url = reverse('report_message', args={self.message.id})

    def test_login_required(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('registration/login.html')

    def test_report(self):
        self.client.login(username='recipient', password='testpass')
        response = self.client.get(self.url)
        self.message.refresh_from_db()
        self.assertTrue(self.message.reported)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/messages/')

    def test_error(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, 'You can not report this message because you are not the recipient.')
