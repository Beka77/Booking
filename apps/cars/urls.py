from django.urls import path 
from .views import car,car_detail

urlpatterns = [ 
    path('cars/',car,name='car'),
    path('cars-detail/<int:id>',car_detail,name='car_detail')
]