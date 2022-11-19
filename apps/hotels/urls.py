from django.urls import path
from .views import hotel_details

urlpatterns = [ 
    path('hotel-details/<int:id>/',hotel_details,name='hotel_details'),
]