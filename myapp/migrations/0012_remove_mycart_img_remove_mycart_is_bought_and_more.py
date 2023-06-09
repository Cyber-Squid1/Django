# Generated by Django 4.1.7 on 2023-06-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0011_mycart_orderid_products_vendorid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mycart",
            name="img",
        ),
        migrations.RemoveField(
            model_name="mycart",
            name="is_bought",
        ),
        migrations.RemoveField(
            model_name="mycart",
            name="name",
        ),
        migrations.RemoveField(
            model_name="mycart",
            name="price",
        ),
        migrations.RemoveField(
            model_name="order",
            name="productid",
        ),
        migrations.RemoveField(
            model_name="order",
            name="productqty",
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(default="", max_length=200),
        ),
    ]