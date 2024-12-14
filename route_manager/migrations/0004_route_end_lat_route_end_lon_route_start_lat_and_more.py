# Generated by Django 5.1.1 on 2024-12-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_manager', '0003_remove_route_end_lat_remove_route_end_lon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='end_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='end_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='start_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='start_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='busstop',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='busstop',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]