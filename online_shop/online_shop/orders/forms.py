from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError

from online_shop.orders.models import Order
from online_shop.web.models import Discount


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['discount_code'].required = False

    def clean_discount_code(self):
        discount_code = self.cleaned_data.get('discount_code')

        if not discount_code:
            return discount_code

        try:
            discount = Discount.objects.get(code=discount_code, user=self.request.user)
        except Discount.DoesNotExist:
            raise ValidationError('Invalid discount code.')

        return discount_code

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'delivery_type',
            'delivery_company',
            'address',
            'discount_code'
        )
