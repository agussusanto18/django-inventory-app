from django.contrib import admin
from app_admin.models import Item, Reservation, ItemReservation


class ItemAdmin(admin.ModelAdmin):
    model = Item

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation

class ItemReservationAdmin(admin.ModelAdmin):
    model = ItemReservation

admin.site.register(Item, ItemAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ItemReservation, ItemReservationAdmin)