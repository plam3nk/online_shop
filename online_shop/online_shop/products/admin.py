from django.contrib import admin

from online_shop.products.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('capitalized_name', 'capitalized_description', 'formatted_price')
    ordering = ('-id',)

    def capitalized_name(self, obj):
        return obj.name.title()

    capitalized_name.short_description = 'Name'

    def capitalized_description(self, obj):
        return obj.description.title()

    @staticmethod
    def formatted_price(obj):
        return f'{obj.price:.2f}$'

    capitalized_description.short_description = 'Description'
