from django.urls import path

from online_shop.products.views import ProductCreateView, ProductDetailsView, ProductEditView, ProductDeleteView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('details/<int:pk>', ProductDetailsView.as_view(), name='details_product'),
    path('edit/<int:pk>', ProductEditView.as_view(), name='edit_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product')
]