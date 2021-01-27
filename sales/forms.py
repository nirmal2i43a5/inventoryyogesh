from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import *


class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class SaleItemForm(ModelForm):
    class Meta:
        model=SalesItem
        fields=['product','quantity']


SaleItemFormset=inlineformset_factory(Sales,SalesItem, form=SaleItemForm,extra=2)