from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Supplier
@login_required
def supplier_list(request):
    supplier=Supplier.objects.all()
    return render(request,'supplier/supplier_list.html',{'supplier':supplier})


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    template_name = "supplier/supplier_form.html"
    fields = '__all__'
    success_message = "New supplier successfully added."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ProductCreateView, self).get_form()
        form.fields['name'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['email'].widget = widgets.EmailInput(attrs={'rows': 1})

        return form


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    template_name = "supplier/supplier_form.html"
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        form = super(SupplierUpdateView, self).get_form()
        form.fields['name'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['email'].widget = widgets.EmailInput(attrs={'rows': 1})

        return form


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = "supplier/supplier_confirm_delete.html"
    success_url = reverse_lazy('supplier-list')
