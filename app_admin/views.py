from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.helpers import is_admin
from app_admin.models import Item, Reservation


@login_required(login_url='/signin/')
def home(request):
    if is_admin(request.user):
        return render(request, 'app_admin/index.html')
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def item_list(request):
    if is_admin(request.user):
        items = Item.objects.all().order_by('-id')
        context = {'items': items}
        return render(request, 'app_admin/item-list.html', context)
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def item_create(request):
    if is_admin(request.user):
        return render(request, 'app_admin/item-create.html')
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def item_delete(request, pk):
    if is_admin(request.user):
        result = Item.objects.filter(pk=pk)
        result.delete()

        return redirect('item-list')
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def user_list(request):
    if is_admin(request.user):
        return render(request, 'app_admin/user-list.html')
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def reservation_list(request):
    if is_admin(request.user):
        reservations = Reservation.objects.all().order_by('-id')
        context = {"reservations": reservations}
        return render(request, 'app_admin/reservation-list.html', context)
    else:
        return redirect('user-home')
