# Generated by Django 5.1.5 on 2025-02-04 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artifacts", "0009_filter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artifactmodel",
            name="lessonPlan",
            field=models.CharField(default="null", max_length=255),
            preserve_default=False,
        ),
    ]
