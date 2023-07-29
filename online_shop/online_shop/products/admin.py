from django.contrib import admin

from online_shop.products.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
