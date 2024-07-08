from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from account.forms import UserForm


class TestUserCreate(TestCase):
    def test_valid_data_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
        self.assertIsInstance(response.context['form'], UserForm)

    def test_valid_data_POST(self):
        response = self.client.post(reverse('register'),
                                    data={'username': 'sampleusername', 'email': '', 'password': 'samplepass'})
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_data_POST(self):
        response = self.client.post(reverse('register'), data={'username': '', 'email': '', 'password': 'samplepass'})
        self.assertFalse(response.context['form'].is_valid())
