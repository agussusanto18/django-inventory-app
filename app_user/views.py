from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from constants.enums import UserRole
from django.contrib.auth.decorators import login_required


@login_required(login_url='/signin/')
def home(request):
    return render(request, 'app_user/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            groupName = UserRole.ADMIN.value
            group = Group.objects.get(name=groupName)

            if group in user.groups.all():
                return redirect('admin-home')
            else:
                return redirect('user-home')
        else:
           return redirect('signin')
    else:
        return render(request, 'app_user/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')