# Generated by Django 5.1.2 on 2024-11-13 01:13

from django.db import migrations, models

import common.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                    "code",
                    models.CharField(
                        db_index=True,
                        default=common.models.generate_code,
                        editable=False,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("street", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("zip_code", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DocumentType",
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
                    "code",
                    models.CharField(
                        db_index=True,
                        default=common.models.generate_code,
                        editable=False,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Email",
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
                    "code",
                    models.CharField(
                        db_index=True,
                        default=common.models.generate_code,
                        editable=False,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="File",
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
                    "code",
                    models.CharField(
                        db_index=True,
                        default=common.models.generate_code,
                        editable=False,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("file", models.FileField(upload_to=common.models.upload_path)),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("NOT_DEFINED", "Not Defined"),
                            ("ACCOUNT_IMAGE", "Account Image"),
                        ],
                        default="NOT_DEFINED",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Phone",
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
                    "code",
                    models.CharField(
                        db_index=True,
                        default=common.models.generate_code,
                        editable=False,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("number", models.CharField(max_length=20)),
                ("ddi", models.CharField(max_length=20)),
                ("ddd", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
