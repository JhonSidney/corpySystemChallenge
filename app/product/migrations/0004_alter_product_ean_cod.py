# Generated by Django 4.2.11 on 2024-03-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_ean_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ean_cod',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
    ]