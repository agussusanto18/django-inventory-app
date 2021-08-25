from django import forms
from app_admin.models import Item, ItemReservation, Reservation, Technician


class ItemForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Barang'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga'}))
    stock = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok'}))
    provider = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kode Barang'}))
    unit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))

    class Meta:
        model = Item
        fields = ['name', 'price', 'stock', 'provider', 'unit']

class TechnicianForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    nik = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nik'}))

    class Meta:
        model = Technician
        fields = ['name', 'nik']