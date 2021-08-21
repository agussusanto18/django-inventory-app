from django.dispatch import receiver
from django.db import models
from app_admin.models import Reservation, ItemReservation

@receiver(models.signals.post_save, sender=Reservation)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        item_reservations = ItemReservation.objects.filter(user=instance.user, reservation=None)
        item_reservations.update(reservation=instance)