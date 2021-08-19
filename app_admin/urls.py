from django.urls import path
from app_admin.views import home

urlpatterns = [
    path('', home, name='admin-home'),
]
