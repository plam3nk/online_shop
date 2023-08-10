from django.test import TestCase
from django.contrib.auth import get_user_model

from online_shop.accounts.forms import ProfileEditForm

UserModel = get_user_model()


class ProfileEditFormTest(TestCase):

    def test_form_valid_data(self):
        user = UserModel.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='test@example.com',
            phone_number='1234567890'
        )

        form_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'phone_number': '9876543210',
        }
        form = ProfileEditForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        user = UserModel.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='test@example.com',
            phone_number='1234567890'
        )

        form_data = {
            'first_name': '',  # Missing first name
            'last_name': 'User',
            'email': 'invalidemail',
            'phone_number': '123',  # Invalid phone number
        }
        form = ProfileEditForm(data=form_data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Check for specific validation errors
