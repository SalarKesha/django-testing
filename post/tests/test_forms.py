from django.contrib.auth.models import User
from django.test import TestCase
from post.forms import PostForm


class TestPostForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root', password='password')

    def test_valid_data(self):
        form = PostForm(data={'title': 'sample', 'content': 'sample'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = PostForm(data={'title': 'sample', 'content': ''})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('content'))

