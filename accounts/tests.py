from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from model_bakery import baker


# Model Tests

class CustomUserModelTests(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.testuser2 = baker.make('accounts.CustomUser')
        self.testuser3 = baker.make('accounts.CustomUser')

    def test_followers_count(self):
        self.testuser2.following.set([self.testuser])
        self.testuser3.following.set([self.testuser])
        self.assertEqual(CustomUser.objects.filter(
            following=self.testuser.id).count(), 2)

    def test_following_count(self):
        self.testuser.following.set([self.testuser2, self.testuser3])
        self.assertEqual(self.testuser.following.count(), 2)


# View Tests

class EditProfileTests(TestCase):

    def setUp(self):
        self.testuser = baker.make('accounts.CustomUser')
        self.client.login(
            username=self.testuser.username, password=self.testuser.password)
        self.url = reverse('edit_profile', kwargs={'pk': self.testuser.pk})
        self.response = self.client.post(self.url, {})

    def test_success_url(self):
        self.assertEqual(
            self.response.context['view'].get_success_url(),
            f'/u/{self.testuser.username}'
        )


class ChangePasswordTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('password')

    def test_post(self):
        self.response = self.client.post(self.url, {
            'old_password': 'testpass',
            'new_password1': 'newtestpass',
            'new_password2': 'newtestpass',
        })
        self.assertEqual(self.response.status_code, 302)
        self.testuser.refresh_from_db()
        self.assertTrue(self.testuser.check_password('newtestpass'))

    def test_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'accounts/password.html')


class DeleteAccountTests(TestCase):

    def setUp(self):
        self.testuser = CustomUser.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('delete_account')

    def test_post(self):
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_error(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'error.html')
        self.assertContains(
            self.response, 'You do not have permission to do this.')
