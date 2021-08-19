from django.contrib import admin
from app_user.models import UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail


admin.site.register(UserDetail, UserDetailAdmin)