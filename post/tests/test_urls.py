from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from post.models import Post
from post.views import PostListView, UserPostView, PostView


class TestUrls(TestCase):
    def test_home(self):
        self.assertEqual(resolve(reverse('home')).func.view_class, PostListView)

    def test_post(self):
        user = User.objects.create_user(username='root', password='password')
        post = Post.objects.create(title='title', content='content', creator=user)
        self.assertEqual(resolve(reverse('post', args=(post.id, ))).func.view_class, PostView)

    def test_user_post(self):
        self.assertEqual(resolve(reverse('create_post')).func.view_class, UserPostView)
