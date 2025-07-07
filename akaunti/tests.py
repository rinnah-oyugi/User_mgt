from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAccountTests(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'akaunti/register.html')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'REE',
            'email': 'reeoyugi@gmail.com',
            'password1': '123asd45',
            'password2': '123asd45'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue(User.objects.filter(username='REE').exists())

    def test_login_view(self):
        user = User.objects.create_user(username='dee', password='deeoyugi@gmail.com')
        response = self.client.post(reverse('login'), {
            'username': 'dee',
            'password': '123asd45'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after login

    def test_profile_access_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, '/login/?next=/profile/')
