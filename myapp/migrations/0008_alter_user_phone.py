# Generated by Django 4.1.7 on 2023-06-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_mycart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.BigIntegerField(),
        ),
    ]
