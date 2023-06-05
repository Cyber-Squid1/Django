# Generated by Django 4.1.7 on 2023-06-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyCart",
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
                ("userId", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("price", models.CharField(max_length=200)),
                ("quantity", models.CharField(max_length=200)),
                ("totalprice", models.CharField(max_length=200)),
                ("is_bought", models.CharField(max_length=200)),
            ],
        ),
    ]
