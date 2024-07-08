from django.urls import resolve, reverse
from django.test import SimpleTestCase
from account.views import UserCreate


class TestUrls(SimpleTestCase):
    def test_register(self):
        self.assertEqual(resolve(reverse('register')).func.view_class, UserCreate)
