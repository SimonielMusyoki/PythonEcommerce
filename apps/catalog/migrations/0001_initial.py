# Generated by Django 4.2 on 2023-04-18 12:18

import apps.catalog.models.products
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.catalog.models.products.upload_image_path)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_digital', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('product_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/simoniel/Dev/Projects/static/protected_media'), upload_to=apps.catalog.models.products.upload_product_file_loc)),
                ('filepath', models.TextField()),
                ('free', models.BooleanField(default=False)),
                ('user_required', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
