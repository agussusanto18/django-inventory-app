from django.urls import path
from app_user.views import home

urlpatterns = [
    path('', home, name='user-home'),
]
