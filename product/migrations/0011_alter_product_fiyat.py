# Generated by Django 3.2 on 2021-04-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fiyat',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]
