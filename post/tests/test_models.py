from django.contrib.auth.models import User
from django.test import TestCase
from post.models import Post


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')

    def test_create(self):
        post = Post.objects.create(title='sample', content='sample', creator=self.user)
        self.assertEqual(str(post), 'sample')
