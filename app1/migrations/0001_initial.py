# Generated by Django 4.2.6 on 2023-10-26 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('brand', models.CharField(max_length=15, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_bestseller', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('category', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='product-img')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('slug', models.SlugField(blank=True)),
                ('is_bestseller', models.BooleanField(blank=True, default=False)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.brand')),
            ],
        ),
    ]
