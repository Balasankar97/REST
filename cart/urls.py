from django.urls import path, include
from .views import *

urlpatterns = [

    path('customers/', CustomerListView.as_view(),name=''),
    path('customers/detail/<int:pk>',CustomerDetailView.as_view(),name="customer_detail"),
    path('orders/',OrderListView.as_view(),name=""),
    path('orders/detail/<int:pk>',OrderDetailView.as_view(),name="order_detail")



]
