from django.db import models
from django.contrib.auth.models import User
from constants.choices import ReservationStatus


class Item(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    nik = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    status = models.IntegerField(choices=ReservationStatus.choices, default=ReservationStatus.PANDING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nik
    

class ItemReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.CharField(max_length=80, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True)
    unit = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name
    