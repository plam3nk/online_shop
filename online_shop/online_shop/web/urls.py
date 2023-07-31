from django.urls import path

from online_shop.web.views import IndexPage, ShopPage, contact_page, testimonial_page, why_page

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('shop/', ShopPage.as_view(), name='shop_page'),
    path('contact/', contact_page, name='contact_page'),
    path('testimonial/', testimonial_page, name='testimonial_page'),
    path('why/', why_page, name='why_page'),
]