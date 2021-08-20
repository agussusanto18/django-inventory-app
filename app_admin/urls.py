from django.urls import path
from app_admin.views import (
    home, item_list, item_create, item_update, 
    item_delete, reservation_detail, user_list, reservation_list,
    reservation_approve, reservation_reject
)

urlpatterns = [
    path('', home, name='admin-home'),
    path('barang/list/', item_list, name='item-list'),
    path('barang/create/', item_create, name='item-create'),
    path('barang/update/<int:pk>/', item_update, name='item-update'),
    path('barang/delete/<int:pk>/', item_delete, name='item-delete'),
    path('user/list/', user_list, name='user-list'),
    path('reservation/list/', reservation_list, name='reservation-list'),
    path('reservation/detail/<int:pk>/', reservation_detail, name='reservation-detail'),

    path('reservation/approve/<int:pk>/', reservation_approve, name='reservation-approve'),
    path('reservation/reject/<int:pk>/', reservation_reject, name='reservation-reject'),
]