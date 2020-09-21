# Generated by Django 3.1.1 on 2020-09-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='product',
            name='date_registered',
            field=models.DateField(auto_now_add=True),
        ),
    ]