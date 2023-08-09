from django.urls import path, include

from online_shop.web.views import IndexPageView, ShopPageView, ContactPageView, WhyPageView, ListContactView, \
    DeleteContactView, TestimonialsPageView, CreateTestimonialPageView

urlpatterns = (
    path('', IndexPageView.as_view(), name='index'),
    path('shop/', ShopPageView.as_view(), name='shop_page'),
    path('why/', WhyPageView.as_view(), name='why_page'),
    path('review/', TestimonialsPageView.as_view(), name='testimonials'),
    path('review/create', CreateTestimonialPageView.as_view(), name='create-testimonial'),
    path('contact/', include([
        path('', ContactPageView.as_view(), name='contact_page'),
        path('list/', ListContactView.as_view(), name='list-contacts'),
        path('delete/<int:pk>/', DeleteContactView.as_view(), name='delete-contact'),
    ])),
)
