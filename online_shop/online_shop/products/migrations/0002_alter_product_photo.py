# Generated by Django 4.2.3 on 2023-07-27 19:37

from django.db import migrations, models
import online_shop.products.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='product_photos/', validators=[online_shop.products.validators.validate_file_less_than_5mb]),
        ),
    ]
