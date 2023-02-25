# Generated by Django 4.1.7 on 2023-02-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("guests_number", models.IntegerField(verbose_name="guests_number")),
                ("booking_date", models.DateTimeField(verbose_name="booking date")),
            ],
            options={
                "verbose_name": "booking",
                "verbose_name_plural": "bookings",
            },
        ),
        migrations.CreateModel(
            name="Menu",
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
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="price"
                    ),
                ),
                ("inventory", models.IntegerField(verbose_name="inventory")),
            ],
            options={
                "verbose_name": "menu",
                "verbose_name_plural": "menus",
            },
        ),
    ]