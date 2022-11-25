from django.urls import path
from apps.cruises.views import cruise

urlpatterns = [ 
    path('cruises/',cruise,name='cruises'),
]