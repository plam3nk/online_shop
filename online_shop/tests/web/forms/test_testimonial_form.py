from django.test import TestCase

from online_shop.web.forms import TestimonialForm


class TestimonialFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'rating': 5,
            'comment': 'Excellent!',
        }
        form = TestimonialForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = TestimonialForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
