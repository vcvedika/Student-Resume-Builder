# Generated by Django 4.1 on 2022-11-07 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalInfo",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("website", models.URLField(blank=True)),
                ("mobile", models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="resume",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("website", models.URLField(blank=True)),
                ("mobile", models.PositiveIntegerField(blank=True)),
                ("degree", models.CharField(max_length=100)),
                ("varsity_name", models.CharField(max_length=100)),
                ("passing_year", models.DateField()),
                ("result", models.CharField(blank=True, max_length=10)),
                ("title", models.CharField(blank=True, max_length=100)),
                ("place", models.CharField(blank=True, max_length=100)),
                ("start_date", models.DateField(blank=True)),
                ("end_date", models.DateField(blank=True)),
                ("description", models.TextField(blank=True)),
                ("skill_detail", models.TextField()),
                ("project_detail", models.TextField(blank=True)),
                ("about_detail", models.TextField(blank=True)),
                ("award_detail", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("skill_detail", models.TextField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("project_detail", models.TextField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("title", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                    "degree",
                    models.CharField(
                        choices=[
                            ("Mtech/MA/MSc/MCom/MBA", "Masters"),
                            ("BE/Btech/BA/BSc/BCom", "Bachelor"),
                            ("12th", "High School"),
                        ],
                        max_length=50,
                    ),
                ),
                ("stream", models.CharField(max_length=100)),
                ("passing_year", models.DateField()),
                ("result", models.CharField(max_length=5)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Awards",
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
                ("award_detail", models.TextField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="About",
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
                ("about_detail", models.TextField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resumeGenerator.personalinfo",
                    ),
                ),
            ],
        ),
    ]
