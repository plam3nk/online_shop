from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.orders.forms import OrderCreateForm
from online_shop.orders.models import Order
from online_shop.products.models import Product


# Create your views here.

class OrderCreateView(LoginRequiredMixin, views.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/create-order.html'
    success_url = reverse_lazy('successful-order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs.get('pk')  # Get the 'pk' from the URL parameters
        product = get_object_or_404(Product, pk=product_pk)
        context['product'] = product  # Pass the product to the template context
        return context

    def form_valid(self, form):
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)

        # Set the currently logged-in user as the user for the order
        form.instance.user = self.request.user

        form.instance.product = product
        return super().form_valid(form)


class OrderSuccessfulView(LoginRequiredMixin, views.TemplateView):
    template_name = 'orders/successful-order.html'


@method_decorator(staff_member_required(login_url=reverse_lazy("login user")), name='dispatch')
class AllOrdersView(views.ListView):
    template_name = 'orders/all-orders-admin.html'
    model = Order

    def get_queryset(self):
        queryset = Order.objects.all()

        return queryset


class UserOrdersView(LoginRequiredMixin, views.ListView):
    template_name = 'orders/user-orders.html'
    model = Order

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Order.objects.filter(user_id=user_id)

        return queryset


class DeleteOrderView(LoginRequiredMixin, views.DeleteView):
    model = Order
    template_name = 'orders/delete-order.html'
    success_url = reverse_lazy('index')
