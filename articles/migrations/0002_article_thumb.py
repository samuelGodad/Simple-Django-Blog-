# Generated by Django 4.1.7 on 2023-09-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="thumb",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
    ]
