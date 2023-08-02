from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Contact(models.Model):
    NAME_MAX_LEN = 40
    NAME_MIN_LEN = 2
    PHONE_NUMBER_MAX_LEN = 10
    MESSAGE_MAX_LEN = 300
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
        max_length=MESSAGE_MAX_LEN
    )
