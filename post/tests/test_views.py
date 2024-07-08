from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from post.models import Post


class TestHomeView(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('post/post_list.html')


class TestPostView(TestCase):
    def test_post(self):
        user = User.objects.create_user(username='root', password='password')
        post = Post.objects.create(title='title', content='content', creator=user)
        response = self.client.get(reverse('post', args=(post.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('post/post.html')


class TestUserPostView(TestCase):
    def setUp(self):
        User.objects.create_user(username='root', password='password')
        self.client = Client()
        self.client.login(username='root', password='password')

    def test_GET(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('post/user_post_list.html')

    def test_valid_POST(self):
        response = self.client.post(reverse('create_post'), data={'title': 'sample', 'content': 'sample'})
        self.assertRedirects(response, reverse('create_post'))

    def test_invalid_POST(self):
        response = self.client.post(reverse('create_post'), data={'title': '', 'content': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
