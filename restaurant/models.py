from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    title = models.CharField(_("title"), max_length=255)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    inventory = models.IntegerField(_("inventory"))

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(_("name"), max_length=255)
    guests_number = models.IntegerField(_("guests_number"))
    booking_date = models.DateTimeField(_("booking date"))

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return self.name
