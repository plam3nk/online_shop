from django.core.exceptions import ValidationError


def validate_value_is_all_num(value):
    if not value.isnumeric():
        raise ValidationError('Phone number must contain only numbers!')
