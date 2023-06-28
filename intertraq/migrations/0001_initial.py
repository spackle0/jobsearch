# Generated by Django 4.2.1 on 2023-06-28 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(blank=True, max_length=255)),
                ("industry", models.CharField(blank=True, max_length=100)),
                ("phone_number", models.CharField(blank=True, max_length=15)),
                ("website", models.URLField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Recruiter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("is_independent", models.BooleanField()),
                (
                    "company",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="intertraq.company"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("posted_date", models.DateTimeField(auto_now_add=True)),
                ("company", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="intertraq.company")),
                (
                    "recruiter",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="intertraq.recruiter"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interview",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("purpose", models.CharField(max_length=200)),
                ("date", models.DateTimeField()),
                ("attendees", models.ManyToManyField(blank=True, to="intertraq.recruiter")),
                ("job", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="intertraq.job")),
            ],
        ),
        migrations.CreateModel(
            name="CommunicationLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "job",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="intertraq.job"
                    ),
                ),
                ("recruiter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="intertraq.recruiter")),
            ],
        ),
    ]