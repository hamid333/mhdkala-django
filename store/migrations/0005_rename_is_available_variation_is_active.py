# Generated by Django 3.2.9 on 2021-11-27 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variation_variation_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='is_available',
            new_name='is_active',
        ),
    ]
