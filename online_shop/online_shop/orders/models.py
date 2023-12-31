from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from online_shop.orders.validators import validate_value_is_all_num
from online_shop.products.models import Product

UserModel = get_user_model()


class Order(models.Model):
    DELIVERY_ECONT = 'E'
    DELIVERY_SPEEDY = 'S'

    DELIVERY_TYPE_ADDRESS = 'H'
    DELIVERY_TYPE_OFFICE = 'O'

    DELIVERY_COMPANY_CHOICES = (
        (DELIVERY_ECONT, 'Econt'),
        (DELIVERY_SPEEDY, 'Speedy')
    )

    DELIVERY_TYPE_CHOICES = (
        (DELIVERY_TYPE_ADDRESS, 'Delivery to the door'),
        (DELIVERY_TYPE_OFFICE, 'Delivery to the office'),
    )

    ADDRESS_MAX_LEN = 150
    ADDRESS_MIN_LEN = 10

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    PHONE_NUMBER_MAX_MIN_LEN = 10

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_MIN_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(PHONE_NUMBER_MAX_MIN_LEN),
            validate_value_is_all_num,
        ),
        error_messages={
            'min_length': 'Phone number must have 10 characters.',
            'max_length': 'Phone number must have 10 characters.',
        }
    )

    delivery_type = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        choices=DELIVERY_TYPE_CHOICES,
    )

    delivery_company = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=DELIVERY_COMPANY_CHOICES,
    )

    address = models.CharField(
        null=False,
        blank=False,
        max_length=ADDRESS_MAX_LEN,
        validators=(
            validators.MinLengthValidator(ADDRESS_MIN_LEN),
        )
    )

    is_verified = models.BooleanField(default=False)

    is_done = models.BooleanField(default=False)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    discount_code = models.CharField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'
