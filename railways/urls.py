from django.urls import path, include
from .views import PassengerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('railways',PassengerViewSet)

urlpatterns = [
#For Function Based views
    # path('',views.passenger_list),
    # path('detail/<int:pk>',views.passenger_detail),

    #For Class Based views
    # path('',PassengerListView.as_view(),name = ''),
    # path('detail/<int:pk>',PassengerDetailView.as_view(),name = 'detail_view'),

    #For routers
    path('',include(router.urls))

]
