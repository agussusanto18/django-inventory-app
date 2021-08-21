from django.urls import path
from app_user.views import home, signin, signout, signup, reservation_list, reservation_create, item_reservation_create

urlpatterns = [
    path('', home, name='user-home'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('reservation/list/', reservation_list, name='user-reservation-list'),
    path('reservation/create/', reservation_create, name='user-reservation-create'),
    path('reservation/item/create/', item_reservation_create, name='item-reservation-create')
]
