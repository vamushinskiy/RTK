# Generated by Django 4.2.6 on 2023-11-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(
                blank=True, default="default1.jpg", upload_to="images/"
            ),
        ),
    ]
