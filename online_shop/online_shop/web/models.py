from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Contact(models.Model):
    NAME_MAX_LEN = 40
    NAME_MIN_LEN = 2
    PHONE_NUMBER_MAX_LEN = 10
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
        max_length=PHONE_NUMBER_MAX_LEN,
    )

    message = models.TextField(
        max_length=MESSAGE_MAX_LEN,
        validators=(
            validators.MinLengthValidator(MESSAGE_MIN_LEN),
        )
    )


class Testimonial(models.Model):
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

    comment = models.TextField()
