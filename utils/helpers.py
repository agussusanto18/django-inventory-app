from django.contrib.auth.models import User, Group
from constants.enums import UserRole


def is_admin(user: User) -> bool:
    groupName = UserRole.ADMIN.value
    group = Group.objects.get(name=groupName)

    if group in user.groups.all():
        return True
    else:
        return False