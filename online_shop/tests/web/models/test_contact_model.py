from django.test import TestCase
from django.core.validators import MinLengthValidator

from online_shop.web.models import Contact


class ContactModelTest(TestCase):
    def test_name_max_length(self):
        contact = Contact.objects.create(
            name='N' * Contact.NAME_MAX_LEN,
            email='test@example.com',
            phone_number='1234567890',
            message='Test message',
        )
        max_length = contact._meta.get_field('name').max_length
        self.assertEqual(max_length, Contact.NAME_MAX_LEN)

    def test_phone_number_max_length(self):
        contact = Contact.objects.create(
            name='Test Name',
            email='test@example.com',
            phone_number='1' * Contact.PHONE_NUMBER_MAX_LEN,
            message='Test message',
        )
        max_length = contact._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, Contact.PHONE_NUMBER_MAX_LEN)

    def test_message_min_length(self):
        contact = Contact.objects.create(
            name='Test Name',
            email='test@example.com',
            phone_number='1234567890',
            message='M' * Contact.MESSAGE_MIN_LEN,
        )
        min_length = Contact.MESSAGE_MIN_LEN
        self.assertTrue(len(contact.message) >= min_length)

