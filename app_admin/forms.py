from django import forms
from app_admin.models import Item


class ItemForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Barang'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga'}))
    stock = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok'}))

    class Meta:
        model = Item
        fields = ['name', 'price', 'stock']