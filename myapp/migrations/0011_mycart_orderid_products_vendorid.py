# Generated by Django 4.1.7 on 2023-06-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0010_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="mycart",
            name="orderId",
            field=models.CharField(default="0", max_length=200),
        ),
        migrations.AddField(
            model_name="products",
            name="vendorid",
            field=models.CharField(default="", max_length=200),
        ),
    ]
