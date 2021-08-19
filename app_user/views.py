from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from constants.enums import UserRole
from django.contrib.auth.decorators import login_required
from utils.helpers import is_admin
from app_user.forms import SignUpForm


@login_required(login_url='/signin/')
def home(request):
    if is_admin(request.user):
        return redirect('admin-home')
    else:
        return render(request, 'app_user/index.html')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                if is_admin(user):
                    return redirect('admin-home')
                else:
                    return redirect('user-home')
            else:
                return redirect('signin')
        else:
            return render(request, 'app_user/signin.html')
    else:
        if is_admin(request.user):
            return redirect('admin-home')
        else:
            return redirect('user-home')



@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    return redirect('signin')


def signup(request):
    if not request.user.is_authenticated:
        form = SignUpForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password = form.cleaned_data['password']

                user = User.objects.create_user(
                    username, email, password, first_name=first_name, last_name=last_name, is_active=1)
                if user:
                    return redirect('signin')
                else:
                    return redirect('signup')
            else:
                return redirect('signup')
        else:
            context = {'form': form}
            return render(request, 'app_user/signup.html', context)
    else:
        if is_admin(request.user):
            return redirect('admin-home')
        else:
            return redirect('user-home')
