# Generated by Django 4.2.6 on 2023-11-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appalumnos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="docente",
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
                ("codigo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=65)),
                ("direccion", models.CharField(max_length=30)),
                ("telefono", models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name="materia",
            name="uv",
            field=models.SmallIntegerField(max_length=2),
        ),
    ]
