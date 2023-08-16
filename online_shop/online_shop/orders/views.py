from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from online_shop.orders.forms import OrderCreateForm
from online_shop.orders.models import Order
from online_shop.products.models import Product
from online_shop.web.models import Discount


# Create your views here.

class OrderCreateView(LoginRequiredMixin, views.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/create-order.html'
    success_url = reverse_lazy('successful-order')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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

        discount_code = form.cleaned_data.get('discount_code')
        if discount_code:
            try:
                discount = Discount.objects.get(code=discount_code, user=self.request.user)
                form.instance.discount = discount
            except Discount.DoesNotExist:
                return self.form_invalid(form)

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


class DeleteOrderView(UserPassesTestMixin, views.DeleteView):
    model = Order
    template_name = 'orders/delete-order.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        order = self.get_object()
        user = self.request.user
        return user.is_staff or user.is_superuser or order.user == user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().delete(request, *args, **kwargs)