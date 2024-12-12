# Generated by Django 5.0.6 on 2024-06-09 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venue",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("contact_email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PricingPackage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("package_name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("details", models.TextField()),
                ("contact_email", models.EmailField(max_length=254)),
                (
                    "venue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="packages",
                        to="owner.venue",
                    ),
                ),
            ],
        ),
    ]
