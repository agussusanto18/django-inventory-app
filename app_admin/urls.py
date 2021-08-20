from django.urls import path
from app_admin.views import home, item_list, item_create, item_delete, user_list, reservation_list

urlpatterns = [
    path('', home, name='admin-home'),
    path('barang/list/', item_list, name='item-list'),
    path('barang/create/', item_create, name='item-create'),
    path('barang/delete/<int:pk>/', item_delete, name='item-delete'),
    path('user/list/', user_list, name='user-list'),
    path('reservation/list/', reservation_list, name='reservation-list')
]
