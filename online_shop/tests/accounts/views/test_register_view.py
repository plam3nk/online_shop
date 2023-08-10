from django.test import TestCase, Client
from django.urls import reverse

from online_shop.accounts.models import DMAppUser


class RegisterUserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register user')
        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
        }

        self.invalid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'differentpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalidemail',
            'phone_number': '123456',
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, data=self.valid_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check if the user is created
        self.assertTrue(DMAppUser.objects.filter(username='testuser').exists())

        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)

        # Check if the response redirects to the correct URL
        self.assertRedirects(response, reverse('index'))

    def test_register_user_with_invalid_data(self):
        response = self.client.post(self.register_url, data=self.invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check if the user is not created
        self.assertFalse(DMAppUser.objects.filter(username='testuser').exists())

        # Check if the user is not logged in
        self.assertFalse(response.context['user'].is_authenticated)

        # Check for form errors
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'phone_number',
                             'Phone number must have 10 characters.')
