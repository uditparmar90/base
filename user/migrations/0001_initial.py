# Generated by Django 3.2.12 on 2023-10-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=45)),
                ('full_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]