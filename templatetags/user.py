from django import template
from app_user.models import UserDetail
register = template.Library()

@register.filter
def getUserPhoto(user_id):
    try:
        return UserDetail.objects.get(user__id=user_id).photo
    except:
        return ""
