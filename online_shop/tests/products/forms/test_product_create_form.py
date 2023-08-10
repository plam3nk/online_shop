from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from online_shop.products.forms import ProductCreateForm
from online_shop.products.models import Product


class ProductCreateFormTest(TestCase):
    def test_form_valid(self):
        image_path = 'static/images/favicon.png'
        with open(image_path, 'rb') as image_file:
            image = SimpleUploadedFile("favicon.png", image_file.read(), content_type="image/png")

        form_data = {
            'name': 'Test Product',
            'description': 'A test product description.',
            'price': 19.99,
        }
        files = {'photo': image}
        form = ProductCreateForm(data=form_data, files=files)
        self.assertTrue(form.is_valid())
