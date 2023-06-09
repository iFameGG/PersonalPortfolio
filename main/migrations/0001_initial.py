# Generated by Django 4.2 on 2023-04-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=50)),
                ("github", models.URLField()),
                ("example", models.URLField()),
                ("description", models.TextField()),
                ("tools", models.CharField(max_length=200)),
                ("category", models.CharField(max_length=200)),
            ],
        ),
    ]
