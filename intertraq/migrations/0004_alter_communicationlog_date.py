# Generated by Django 4.2.1 on 2023-06-28 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("intertraq", "0003_alter_communicationlog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communicationlog",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
