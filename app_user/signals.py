from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.db import models
from constants.enums import UserRole
from app_user.models import UserDetail


@receiver(models.signals.pre_save, sender=User)
def create_user_groups(sender, instance, **kwargs):
    if instance._state.adding:
        groups = Group.objects.all()
        if not groups.exists():
            Group.objects.bulk_create([
                Group(name=UserRole.ADMIN.value),
                Group(name=UserRole.USER.value)
            ])


@receiver(models.signals.post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        groupName = UserRole.USER.value
        group = Group.objects.get(name=groupName)
        instance.groups.add(group)
        UserDetail.objects.create(user=instance)
