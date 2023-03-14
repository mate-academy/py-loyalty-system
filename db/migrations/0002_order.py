# Generated by Django 4.1 on 2023-03-14 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_time", models.DateTimeField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=8)),
                ("loyalty_program", models.CharField(max_length=20)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="db.customer"
                    ),
                ),
            ],
        ),
    ]