# Generated by Django 3.2.12 on 2023-10-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_shirts_shirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.CharField(default='Unknown', max_length=15),
        ),
    ]