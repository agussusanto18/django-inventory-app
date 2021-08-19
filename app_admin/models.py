from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ItemReservation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)