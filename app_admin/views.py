from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from utils.helpers import is_admin
from app_admin.models import Item, Reservation, ItemReservation
from app_user.models import UserDetail
from constants.enums import UserRole
from constants.choices import ReservationStatus
from app_admin.forms import ItemForm


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
def reservation_detail(request, pk):
    if is_admin(request.user):
        reservation = Reservation.objects.get(pk=pk)
        reservation_items = ItemReservation.objects.filter(reservation=reservation)
        context = {'reservation': reservation, 'reservation_items': reservation_items}
        return render(request, 'app_admin/reservation-detail.html', context)
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def reservation_approve(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    reservation.update(status=ReservationStatus.APPROVED)
    
    return redirect('reservation-detail', pk=pk)

@login_required(login_url='/signin/')
def reservation_reject(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    reservation.update(status=ReservationStatus.REJECTED)
    
    return redirect('reservation-detail', pk=pk)


@login_required(login_url='/signin/')
def item_create(request):
    if is_admin(request.user):
        form = ItemForm(request.POST or None)
        
        if request.method == 'POST':
            if form.is_valid():
                result = form.save()
                
                if result:
                    return redirect('item-list') 

        return render(request, 'app_admin/item-form.html', {
            'form': form,
            'title': 'Tambah Barang'
        })
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def item_update(request, pk):
    if is_admin(request.user):
        instance = Item.objects.get(pk=pk)
        form = ItemForm(request.POST or None, instance=instance)
        
        if request.method == 'POST':
            if form.is_valid():
                result = form.save()
                
                if result:
                    return redirect('item-list') 

        return render(request, 'app_admin/item-form.html', {
            'form': form,
            'title': 'Update Barang'
        })
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
        users = UserDetail.objects.filter(user__groups__name=UserRole.USER.value)
        context = {
            'users': users
        }

        return render(request, 'app_admin/user-list.html', context)
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