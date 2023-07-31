from django import forms

from online_shop.orders.models import Orders


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'delivery_type', 'delivery_company', 'address')
