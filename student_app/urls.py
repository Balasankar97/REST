from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.student_list),
    path('detail/<int:pk>',views.student_detail),


]
