from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from online_shop.products.models import Product
from online_shop.products.views import ProductDetailsView


class ProductDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        image_content = b'\x89PNG\r\n\x1a\n...'
        image_file = SimpleUploadedFile("test_image.png", image_content, content_type="image/png")

        self.product = Product.objects.create(
            name='Test Product',
            description='A test product',
            price=10.99,
            photo=image_file,
        )

    def test_get_request_renders_template(self):
        response = self.client.get(reverse('details_product', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/details-product.html')

    def test_context_contains_product_pk(self):
        response = self.client.get(reverse('details_product', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pk'], self.product.pk)

