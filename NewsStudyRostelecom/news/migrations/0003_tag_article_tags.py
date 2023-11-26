# Generated by Django 4.2.6 on 2023-11-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_article_options_alter_article_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=80)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
                "ordering": ["title", "status"],
            },
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(blank=True, to="news.tag"),
        ),
    ]
