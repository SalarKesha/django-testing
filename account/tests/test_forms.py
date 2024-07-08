from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from account.forms import UserForm
from django.test import TestCase


class TestRegisterForm(TestCase):
    def setUp(self):
        User.objects.create_user(username='root', email='root@email.com', password='12345678')

    def test_valid_data(self):
        form = UserForm(data={'username': 'sampleusername', 'email': 'sample@email.com', 'password': 'samplepassword'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_duplicate_email(self):
        form = UserForm(data={'username': 'sampleusername', 'email': 'root@email.com', 'password': 'samplepassword'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))
