# Generated by Django 4.2.3 on 2023-08-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
