# Generated by Django 4.2.16 on 2024-09-23 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_remove_stores_product_name_remove_stores_benefits_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stores',
            new_name='store',
        ),
    ]
