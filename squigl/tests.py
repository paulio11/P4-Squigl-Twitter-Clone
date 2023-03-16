from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password


class SettingsTests(TestCase):

    def test_debug_is_false(self):
        self.assertEqual(settings.DEBUG, False)

    def test_secret_key_strength(self):
        is_strong = validate_password(settings.SECRET_KEY)
