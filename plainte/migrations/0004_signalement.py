# Generated by Django 5.1.7 on 2025-03-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plainte", "0003_remove_report_photo_alter_report_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Signalement",
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
                ("category", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
