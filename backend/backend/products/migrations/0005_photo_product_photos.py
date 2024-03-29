# Generated by Django 4.2.9 on 2024-02-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_status_product_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.ManyToManyField(to='products.photo'),
        ),
    ]
