# Generated by Django 4.1 on 2023-03-14 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0002_order"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Order",
        ),
    ]
