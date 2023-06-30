# Generated by Django 4.1.7 on 2023-06-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0012_remove_mycart_img_remove_mycart_is_bought_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VendorRegister",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.IntegerField()),
            ],
        ),
    ]
