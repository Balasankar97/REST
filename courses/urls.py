from django.urls import path, include
from .views import CoursesListView, CoursesDetailView

urlpatterns = [

    path('',CoursesListView.as_view(),name = ''),
    path('detail/<int:pk>',CoursesDetailView.as_view(),name = 'detail_view'),

]
