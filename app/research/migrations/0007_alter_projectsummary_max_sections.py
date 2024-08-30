# Generated by Django 4.2.13 on 2024-06-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("research", "0006_projectsummary_sentence_limit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectsummary",
            name="max_sections",
            field=models.IntegerField(default=5, verbose_name="Summary Maximum Sections per Topic"),
        ),
    ]
