from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.passenger_list),
    path('detail/<int:pk>',views.passenger_detail),

]
