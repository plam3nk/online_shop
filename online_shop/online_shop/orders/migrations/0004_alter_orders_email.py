# Generated by Django 4.2.3 on 2023-07-31 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
