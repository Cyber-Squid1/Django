# Generated by Django 4.1.7 on 2023-05-23 18:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0016_feedback"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
    ]
