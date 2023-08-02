from django.urls import path

from online_shop.orders.views import AllOrdersView, OrderSuccessfulView, OrderCreateView, UserOrdersView, \
    DeleteOrderView

urlpatterns = (
    path('', AllOrdersView.as_view(), name='all-orders'),
    path('create/<int:pk>', OrderCreateView.as_view(), name='create-order'),
    path('successful/', OrderSuccessfulView.as_view(), name='successful-order'),
    path('my_orders/', UserOrdersView.as_view(), name='user-orders'),
    path('delete/<int:pk>/', DeleteOrderView.as_view(), name='delete-order')
)
