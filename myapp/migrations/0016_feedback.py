# Generated by Django 4.1.7 on 2023-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0015_rename_id_products_productid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phonenumber", models.IntegerField()),
                ("message", models.CharField(max_length=1000)),
            ],
        ),
    ]
