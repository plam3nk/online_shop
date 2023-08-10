from django.contrib import admin

from online_shop.web.models import Contact, Testimonial


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('capitalized_name', 'email', 'phone_number', 'capitalized_message')
    ordering = ('-id',)

    def capitalized_name(self, obj):
        return obj.name.title()

    capitalized_name.short_description = 'Name'

    def capitalized_message(self, obj):
        return obj.message.title()

    capitalized_message.short_description = 'Message'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment')
    ordering = ('-id',)

