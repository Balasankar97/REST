from django.urls import path, include
#from .views import CoursesListView, CoursesDetailView
from .views import CourseViewSet
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('', CourseViewSet)

urlpatterns = [

    # path('',CoursesListView.as_view(),name = ''),
    # path('detail/<int:pk>',CoursesDetailView.as_view(),name = 'detail_view'),

    #For viewsets
    path('courses',include(router.urls))

]
