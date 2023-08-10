from django.test import TestCase
from django.core import validators
from django.contrib.auth import get_user_model
from online_shop.products.models import Product
from online_shop.orders.models import Order

UserModel = get_user_model()


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name='Test Product',
            photo='test.jpg',
            description='Test description',
            price=10.00,
        )
        cls.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
        )

    def test_first_name_max_length(self):
        order = Order.objects.create(
            first_name='F' * Order.FIRST_NAME_MAX_LEN,
            last_name='Last Name',
            email='test@example.com',
            phone_number='1234567890',
            delivery_type=Order.DELIVERY_TYPE_ADDRESS,
            delivery_company=Order.DELIVERY_ECONT,
            address='Test Address',
            product=self.product,
            user=self.user,
        )
        max_length = order._meta.get_field('first_name').max_length
        self.assertEqual(max_length, Order.FIRST_NAME_MAX_LEN)
