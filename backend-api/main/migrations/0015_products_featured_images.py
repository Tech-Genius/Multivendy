# Generated by Django 4.1.2 on 2022-11-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_products_category_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured_images',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]