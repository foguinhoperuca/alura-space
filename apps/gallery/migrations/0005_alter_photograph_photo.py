# Generated by Django 5.1.7 on 2025-03-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0004_photograph_photo_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photograph",
            name="photo",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
        ),
    ]
