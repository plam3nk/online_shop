from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from online_shop.orders.models import Order


# Register your models here.


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'contact',
        'is_verified',
        'is_done',
        'product_name',
        'user_name',
    )

    list_display_links = (
        'full_name',
        'product_name',
        'user_name',
    )

    ordering = (
        'is_verified',
        'is_done',
        '-id'
    )

    @staticmethod
    def full_name(order):
        return order.first_name + ' ' + order.last_name

    @staticmethod
    def contact(order):
        return order.email + '/' + order.phone_number

    def product_name(self, obj):
        if obj.product:
            url = reverse('admin:%s_%s_change' % (obj.product._meta.app_label, obj.product._meta.model_name),
                          args=[obj.product.id])
            return format_html('<a href="{}">{}</a>', url, obj.product.name.title())
        return '-'

    product_name.short_description = 'Product'

    def user_name(self, obj):
        if obj.user:
            url = reverse('admin:%s_%s_change' % (obj.user._meta.app_label, obj.user._meta.model_name),
                          args=[obj.user.id])
            return format_html('<a href="{}">{}</a>', url, obj.user.username.title())
        return '-'

    user_name.short_description = 'User'