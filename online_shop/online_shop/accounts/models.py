from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.

class DMAppUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    PHONE_NUMBER_MAX_MIN_LEN = 10
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
        )
    )

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_MIN_LEN,
        validators=(
            validators.MinLengthValidator(PHONE_NUMBER_MAX_MIN_LEN),
        )
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'

        return None
