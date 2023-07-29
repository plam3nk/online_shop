from django.core.exceptions import ValidationError


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def validate_file_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')


def validate_value_is_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('Price must be higher than 0')

    return value