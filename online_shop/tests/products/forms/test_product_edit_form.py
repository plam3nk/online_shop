from django.test import TestCase
from online_shop.products.forms import ProductEditForm
from online_shop.products.models import Product


class ProductEditFormTest(TestCase):
    def test_form_fields(self):
        form = ProductEditForm()
        self.assertTrue('name' in form.fields)
        self.assertTrue('description' in form.fields)
        self.assertTrue('price' in form.fields)
        self.assertTrue('photo' in form.fields)

    def test_form_placeholders(self):
        form = ProductEditForm()
        self.assertEqual(form.fields['name'].widget.attrs['placeholder'], "Enter product name")
        self.assertEqual(form.fields['description'].widget.attrs['placeholder'], "Enter product description")
        self.assertEqual(form.fields['price'].widget.attrs['placeholder'], "Enter product price")

    def test_form_required_fields(self):
        form = ProductEditForm()
        self.assertFalse(form.fields['name'].required)
        self.assertFalse(form.fields['description'].required)
        self.assertFalse(form.fields['price'].required)
        self.assertFalse(form.fields['photo'].required)
