# Generated by Django 4.1.7 on 2023-09-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_article_thumb"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="audio",
            field=models.FileField(blank=True, upload_to="audio/"),
        ),
        migrations.AddField(
            model_name="article",
            name="video",
            field=models.FileField(blank=True, upload_to="video/"),
        ),
    ]