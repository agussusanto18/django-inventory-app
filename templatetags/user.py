from django import template
from app_user.models import UserDetail
from constants.enums import UserRole
register = template.Library()

@register.filter
def getUserPhoto(user_id):
    try:
        return UserDetail.objects.get(user__id=user_id).photo
    except:
        return ""

@register.filter
def is_admin(user):
    return user.groups.filter(name=UserRole.ADMIN.value).exists()