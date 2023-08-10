from django.test import TestCase
from django.contrib.auth import get_user_model

from online_shop.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class RegisterUserFormTest(TestCase):

    def test_form_valid_data(self):
        form_data = {
            'username': 'john',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'invalidemail',
            'phone_number': '123',
            'password1': 'securepassword123',
            'password2': 'differentpassword',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Check for specific validation errors
