# Generated by Django 4.2.16 on 2024-09-23 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_stores_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='Product_name',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='benefits',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='details',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='ethics',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='qualities',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='values',
        ),
    ]
