from django.urls import path
from app_user.views import home, signin, signout, signup

urlpatterns = [
    path('', home, name='user-home'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
]
