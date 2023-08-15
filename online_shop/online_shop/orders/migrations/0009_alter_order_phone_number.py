# Generated by Django 4.2.3 on 2023-08-15 21:43

import django.core.validators
from django.db import migrations, models
import online_shop.orders.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_discount_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), online_shop.orders.validators.validate_value_is_all_num]),
        ),
    ]
