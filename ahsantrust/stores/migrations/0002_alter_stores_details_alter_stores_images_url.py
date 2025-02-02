# Generated by Django 5.0.7 on 2024-07-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stores",
            name="details",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="stores",
            name="images_url",
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
