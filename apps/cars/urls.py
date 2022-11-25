from django.urls import path 
from .views import car

urlpatterns = [ 
    path('cars/',car,name='car'),
]