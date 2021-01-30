from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import *
from Inventory.models import Product


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'

class SaleItemForm(ModelForm):
    class Meta:
        model=SalesItem
        fields=['product','quantity']


SaleItemFormset=inlineformset_factory(Sales,SalesItem, form=SaleItemForm,extra=1, max_num=Product.objects.count())


'''    $('.formset_row').formset({
		addText: '<button class="btn btn-warning">Add item </button>',
        deleteText: 'Remove',
        prefix: 'items'
    });

$('select').select2()

'''