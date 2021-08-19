from django.db import models
from django.utils.translation import gettext_lazy as _


class ReservationStatus(models.IntegerChoices):
    APPROVED = 1, _('APPROVED')
    PANDING = 2, _('PANDING')
    REJECTED = 3, _('REJECTED')


class Gender(models.TextChoices):
    MALE = 'L', _('LAKI-LAKI')
    FAMALE = 'P', _('PEREMPUAN')
