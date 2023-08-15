from django.core import validators
from django.db import models

from online_shop.products.validators import validate_file_less_than_5mb, validate_value_is_greater_than_zero


# Create your models here.

class Product(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    DESC_MAX_LEN = 300
    DESC_MIN_LEN = 10
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
        )
    )

    photo = models.ImageField(
        upload_to='product_photos/',
        null=False,
        blank=False,
        validators=(
            validate_file_less_than_5mb,
        )
    )

    description = models.CharField(
        max_length=DESC_MAX_LEN,
        validators=(
            validators.MinLengthValidator(DESC_MIN_LEN),
        )
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validate_value_is_greater_than_zero,
        )
    )

    def __str__(self):
        return f'ID: {self.id} - {self.name.capitalize()}'
