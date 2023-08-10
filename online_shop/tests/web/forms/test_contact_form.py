from django.test import TestCase

from online_shop.web.forms import ContactForm


class ContactFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'test user',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'message': 'This is a test message.',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
