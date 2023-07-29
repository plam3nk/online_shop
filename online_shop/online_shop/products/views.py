from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.products.forms import ProductCreateForm, ProductEditForm
from online_shop.products.models import Product


# Create your views here.
@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class ProductCreateView(views.CreateView):
    model = Product
    template_name = 'products/create-product.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('shop_page')


class ProductEditView(views.UpdateView):
    model = Product
    template_name = 'products/edit-product.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('details_product')

    def get_success_url(self, **kwargs):
        return reverse_lazy('details_product', kwargs={'pk': self.object.pk})


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'products/details-product.html'


class ProductDeleteView(views.DeleteView):
    model = Product
    template_name = 'products/delete-product.html'
