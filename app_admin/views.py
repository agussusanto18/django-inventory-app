from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from utils.helpers import is_admin
from app_admin.models import Item, Reservation, ItemReservation, Technician
from app_user.models import UserDetail
from constants.enums import UserRole
from constants.choices import ReservationStatus
from app_admin.forms import ItemForm, TechnicianForm
from datetime import datetime, timedelta


@login_required(login_url='/signin/')
def home(request):
    if is_admin(request.user):
        context = {
            'total_item': len(Item.objects.all()),
            'total_user': len(User.objects.filter(groups__name=UserRole.USER.value)),
            'total_panding_reservation': len(Reservation.objects.filter(status=ReservationStatus.PANDING)),
            'total_approved_reservation': len(Reservation.objects.filter(status=ReservationStatus.APPROVED))
        }

        return render(request, 'app_admin/index.html', context)
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
@transaction.atomic
def reservation_approve(request, pk):
    # try:
    reservation = Reservation.objects.filter(pk=pk)
    
    if reservation.exists():
        reservation.update(status=ReservationStatus.APPROVED, undo=True)

        new_items =[]
        item_reservations = ItemReservation.objects.filter(reservation=reservation[0])
        
        for item_reservation in item_reservations:
            aItem = item_reservation.item
            aItem.stock = aItem.stock - item_reservation.quantity
            new_items.append(aItem)

        Item.objects.bulk_update(new_items, ['stock']) 
    # except Exception as e:
    #     print(e)

    return redirect('reservation-detail', pk=pk)

@login_required(login_url='/signin/')
def reservation_reject(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    
    if reservation.exists():
        reservation.update(status=ReservationStatus.REJECTED)

        undo = reservation[0].undo
        
        if undo == True:
            new_items =[]
            item_reservations = ItemReservation.objects.filter(reservation=reservation[0])
            
            for item_reservation in item_reservations:
                aItem = item_reservation.item
                aItem.stock = aItem.stock + item_reservation.quantity
                new_items.append(aItem)

            Item.objects.bulk_update(new_items, ['stock']) 

    
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
def user_detail(request, pk):
    if is_admin(request.user):
        userdetail = UserDetail.objects.get(user__pk=pk)
        reservations = Reservation.objects.filter(user=userdetail.user)

        context = {
            'userdetail': userdetail,
            'reservations': reservations,
            'is_admin': is_admin(userdetail.user)
        }

        return render(request, 'app_admin/user-detail.html', context)
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def reservation_list(request):
    if is_admin(request.user):
        reservations = Reservation.objects.all().order_by('-created')
        context = {"reservations": reservations}
        return render(request, 'app_admin/reservation-list.html', context)
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def print_pdf(request):
    if is_admin(request.user):
        days = request.GET.get('days', None)
        allData = request.GET.get('all', None)
        reservations = []

        if allData:
            queryset = Reservation.objects.all()
        else:
            if days:
                startdate = datetime.today()
                enddate = startdate - timedelta(days=int(days))
                queryset = Reservation.objects.filter(created__range=[startdate, enddate])
            else:
                queryset = Reservation.objects.all()

        for reservation in queryset:
            item_reservations = ItemReservation.objects.filter(reservation=reservation)
            reservations.append({
                'reservation': reservation,
                'items': item_reservations
            })
        return render(request, 'app_admin/export-reservation.html', {
            'reservations': reservations
        })
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def reservation_detail_print(request, pk):
    if is_admin(request.user):
        reservation = Reservation.objects.get(pk=pk)
        reservation_items = ItemReservation.objects.filter(reservation=reservation)
        context = {'reservation': reservation, 'reservation_items': reservation_items}
        return render(request, 'app_admin/export-reservation-detail.html', context)
    else:
        return redirect('user-home')


@login_required(login_url='/signin/')
def technician_list(request):
    if is_admin(request.user):
        technicians = Technician.objects.all().order_by('-id')
        context = {'technicians': technicians}
        return render(request, 'app_admin/technician-list.html', context)
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def technician_create(request):
    if is_admin(request.user):
        form = TechnicianForm(request.POST or None)
        
        if request.method == 'POST':
            if form.is_valid():
                result = form.save()
                
                if result:
                    return redirect('technician-list') 

        return render(request, 'app_admin/technician-form.html', {
            'form': form,
            'title': 'Tambah Teknisi'
        })
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def technician_update(request, pk):
    if is_admin(request.user):
        instance = Technician.objects.get(pk=pk)
        form = TechnicianForm(request.POST or None, instance=instance)
        
        if request.method == 'POST':
            if form.is_valid():
                result = form.save()
                
                if result:
                    return redirect('technician-list') 

        return render(request, 'app_admin/technician-form.html', {
            'form': form,
            'title': 'Update Teknisi'
        })
    else:
        return redirect('user-home')

@login_required(login_url='/signin/')
def technician_delete(request, pk):
    if is_admin(request.user):
        result = Technician.objects.filter(pk=pk)
        result.delete()

        return redirect('technician-list')
    else:
        return redirect('user-home')
