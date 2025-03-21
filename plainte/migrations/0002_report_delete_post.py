# Generated by Django 5.1.7 on 2025-03-14 10:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plainte", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("dechets", "Déchets"),
                            ("route", "Route endommagée"),
                            ("coupure", "Coupure d'eau ou de courant"),
                            ("eclairage", "Éclairage public"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
