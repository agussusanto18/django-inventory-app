from django.urls import path
from app_user.views import (
    home, signin, signout, signup, 
    reservation_list, reservation_detail, reservation_create, 
    item_reservation_create, item_reservation_json, item_reservation_delete_json,
    user_setting, user_detail
)

urlpatterns = [
    path('', home, name='user-home'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('reservation/list/', reservation_list, name='user-reservation-list'),
    path('reservation/detail/<int:pk>/', reservation_detail, name='user-reservation-detail'),
    path('reservation/create/', reservation_create, name='user-reservation-create'),
    path('reservation/item/create/', item_reservation_create, name='item-reservation-create'),
    path('reservation/item/json/', item_reservation_json, name='item-reservation-json'),
    path('reservation/item/delete/json/<int:pk>/', item_reservation_delete_json, name='item-reservation-delete-json'),
    path('setting/', user_setting, name='user-setting'),
    path('profile/', user_detail, name='user-profile')
]
