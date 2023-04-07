# Generated by Django 4.1.7 on 2023-04-07 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streaming", "0003_remove_streamvideo_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video_metadata",
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
                ("metadata", models.CharField(max_length=300)),
            ],
        ),
    ]