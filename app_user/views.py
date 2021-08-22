from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from constants.enums import UserRole
from django.contrib.auth.decorators import login_required
from utils.helpers import is_admin
from app_user.forms import SignUpForm
from app_admin.models import Reservation, ItemReservation, Item
from django.http import JsonResponse


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

        context = {'form': form}
        return render(request, 'app_user/signup.html', context)
    else:
        if is_admin(request.user):
            return redirect('admin-home')
        else:
            return redirect('user-home')

@login_required(login_url='/signin/')
def reservation_list(request):
    if is_admin(request.user):
        return redirect('admin-home')
    else:
        reservations = Reservation.objects.filter(user=request.user).order_by('-id')
        context = {"reservations": reservations}
        return render(request, 'app_user/reservation-list.html', context)

@login_required(login_url='/signin/')
def reservation_create(request):
    if is_admin(request.user):
        return redirect('admin-home')
    else:
        if request.method == 'POST':
            nik = request.POST['nik']
            name = request.POST['name']
            schedule = request.POST['schedule']
            reservation = Reservation.objects.create(
                user=request.user,
                nik=nik,
                name=name,
                schedule=schedule
            ).save()

            if reservation is None:
                return redirect('user-reservation-list')
        else:
            context = {
                'items': Item.objects.all().order_by('-id'),
                'item_reservations': ItemReservation.objects.filter(user=request.user, reservation=None).order_by('-id')
            }

        return render(request, 'app_user/reservation-create.html', context)

@login_required(login_url='/signin/')
def reservation_detail(request, pk):
    if is_admin(request.user):
        return redirect('admin-home')
    else:
        reservation = Reservation.objects.get(pk=pk)
        reservation_items = ItemReservation.objects.filter(reservation=reservation)
        context = {'reservation': reservation, 'reservation_items': reservation_items}
        return render(request, 'app_user/reservation-detail.html', context)

@login_required(login_url='/signin/')
def item_reservation_create(request):
    if is_admin(request.user):
        return redirect('admin-home')
    else:
        print(request.POST)
        try:
            user = request.user
            provider = request.POST['provider']
            item = Item.objects.get(pk=int(request.POST['item']))
            quantity = request.POST['quantity']
            unit = request.POST['unit']
            

            reservation = ItemReservation.objects.create(
                user=user,
                provider=provider,
                item=item,
                quantity=quantity,
                unit=unit
            )

            if reservation.save() is None:
                item_reservations = ItemReservation.objects.filter(user=user, reservation=None).order_by('-id')

                return JsonResponse({'status': 200, 'message': 'Berhasil Ditambahkan'})
            else:
                return JsonResponse({'status': 500, 'message': 'Terjadi Kesalahan'})
        except Exception as e:
            return JsonResponse({'status': 500, 'message': 'Terjadi Kesalahan'})

        return render(request, 'app_user/reservation-create.html')


@login_required(login_url='/signin/')
def item_reservation_json(request):
    item_reservations = ItemReservation.objects.filter(user=request.user, reservation=None).order_by('-id')
    item_json = [{
        'id': item.pk, 
        'provider': item.provider, 
        'item': item.item.name, 
        'quantity': item.quantity, 
        'unit': item.unit
    } for item in item_reservations]

    return JsonResponse(item_json, safe=False)

@login_required(login_url='/signin/')
def item_reservation_delete_json(request, pk):
    item_reservation = ItemReservation.objects.filter(pk=pk)
    item_reservation.delete()

    return JsonResponse({'status': 200, 'message': 'Berhasil di Hapus'})