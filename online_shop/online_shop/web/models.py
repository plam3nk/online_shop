import uuid

from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from online_shop.web.validators import validate_value_is_all_num

# Create your models here.
UserModel = get_user_model()


class Contact(models.Model):
    NAME_MAX_LEN = 40
    NAME_MIN_LEN = 2
    PHONE_NUMBER_MAX_MIN_LEN = 10
    MESSAGE_MAX_LEN = 300
    MESSAGE_MIN_LEN = 10

    name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_MIN_LEN,
        validators=(
            validate_value_is_all_num,
            MinLengthValidator(PHONE_NUMBER_MAX_MIN_LEN),
        ),
        error_messages={
            'min_length': 'Phone number must have 10 characters.',
            'max_length': 'Phone number must have 10 characters.',
        }
    )

    message = models.TextField(
        max_length=MESSAGE_MAX_LEN,
        validators=(
            validators.MinLengthValidator(MESSAGE_MIN_LEN),
        )
    )

    def __str__(self):
        return f'{self.id} - {self.name}'


class Testimonial(models.Model):
    COMMENT_MAX_LEN = 300
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(choices=RATING_CHOICES)

    comment = models.TextField(max_length=COMMENT_MAX_LEN)

    def __str__(self):
        return f'{self.id} - {self.user.username}'


class Discount(models.Model):
    MIN_AMOUNT_VALUE = 1

    code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        error_messages={
            'invalid': 'Invalid discount code.'
        }
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=(
            MinValueValidator(MIN_AMOUNT_VALUE),
        )
    )

    active = models.BooleanField(default=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} - Code: {self.code}"
