# Generated by Django 5.0.6 on 2024-06-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0011_alter_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='contact_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]