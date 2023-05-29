# Generated by Django 4.1.7 on 2023-05-19 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0013_alter_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
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
        migrations.DeleteModel(
            name="Product",
        ),
    ]
