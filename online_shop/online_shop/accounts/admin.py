from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'contact')
    ordering = ('-id', )

    @staticmethod
    def contact(order):
        return order.email + '/' + order.phone_number