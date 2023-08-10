# Generated by Django 4.2.3 on 2023-08-09 17:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_testimonial_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(30)]),
        ),
    ]
