from django import forms

from online_shop.orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'delivery_type', 'delivery_company', 'address')
