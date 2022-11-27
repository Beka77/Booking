from django.urls import path
from .views import all_hotels, hotel_details

urlpatterns = [ 
    path('hotel-details/<int:id>/',hotel_details,name='hotel_details'),
    path('hotels-grid/',all_hotels,name='all_hotels'),
]   