from django.urls import path
from .views import hotel

urlpatterns = [ 
    path('hotel/<int:id>/',hotel,name='hotel_details'),
]