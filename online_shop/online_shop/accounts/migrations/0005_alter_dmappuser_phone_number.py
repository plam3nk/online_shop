# Generated by Django 4.2.3 on 2023-08-09 17:39

import django.core.validators
from django.db import migrations, models
import online_shop.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_dmappuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmappuser',
            name='phone_number',
            field=models.CharField(error_messages={'max_length': 'Phone number must have 10 characters.', 'min_length': 'Phone number must have 10 characters.'}, max_length=10, validators=[django.core.validators.MinLengthValidator(10), online_shop.accounts.validators.validate_value_is_all_num]),
        ),
    ]
