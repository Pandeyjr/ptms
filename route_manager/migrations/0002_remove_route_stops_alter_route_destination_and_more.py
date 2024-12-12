# Generated by Django 5.1.1 on 2024-12-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='stops',
        ),
        migrations.AlterField(
            model_name='route',
            name='destination',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='route',
            name='starting_point',
            field=models.CharField(max_length=255),
        ),
    ]
