# Generated by Django 5.1.6 on 2025-02-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_products_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.TextField(max_length=60),
        ),
    ]
