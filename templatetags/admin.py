from django import template
from app_user.models import UserDetail
from app_admin.models import Reservation
from constants.choices import ReservationStatus
register = template.Library()

@register.filter
def getPandingReservations(value):
    try:
        return Reservation.objects.filter(status=ReservationStatus.PANDING)
    except:
        return ""