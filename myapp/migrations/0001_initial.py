# Generated by Django 4.1.7 on 2023-05-30 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("categoryname", models.CharField(max_length=200)),
                ("img", models.ImageField(upload_to="category")),
            ],
        ),
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
        migrations.CreateModel(
            name="Order",
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
                ("orderDate", models.DateTimeField(auto_created=True, auto_now=True)),
                ("productid", models.CharField(max_length=200)),
                ("productqty", models.CharField(max_length=200)),
                ("userId", models.CharField(max_length=200)),
                ("userName", models.CharField(max_length=200)),
                ("userEmail", models.CharField(max_length=200)),
                ("userContact", models.IntegerField()),
                ("address", models.CharField(max_length=300)),
                ("orderAmount", models.IntegerField()),
                ("paymentMethod", models.CharField(max_length=200)),
                ("transactionId", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("phone", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                ("productid", models.BigAutoField(primary_key=True, serialize=False)),
                ("productname", models.CharField(max_length=200)),
                ("productimg", models.ImageField(upload_to="products")),
                ("price", models.IntegerField(default=0)),
                ("productdescription", models.TextField()),
                ("quantity", models.IntegerField(default=0)),
                (
                    "productcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.category"
                    ),
                ),
            ],
        ),
    ]
