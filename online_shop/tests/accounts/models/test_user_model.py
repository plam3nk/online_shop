from django.core.exceptions import ValidationError
from django.test import TestCase

from online_shop.accounts.models import DMAppUser


class DMAppUserModelTest(TestCase):

    def test_valid_user_model(self):
        user = DMAppUser(
            username='testuser',
            password='testuser321312',
            first_name="Test",
            last_name="User",
            email="test@example.com",
            phone_number="1234567890"  # Valid phone number with 10 digits
        )
        user.full_clean()  # This will validate the model
        user.save()

        self.assertIsNotNone(user.id)

    def test_invalid_user_model(self):
        with self.assertRaises(ValidationError):
            user = DMAppUser(
                first_name="T",
                last_name="S",
                email="jane@",
                phone_number="12345"
            )
            user.full_clean()  # This will trigger a ValidationError