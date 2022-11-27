from django.urls import path
from .views import cruise,cruise_detail

urlpatterns = [ 
    path('cruise/',cruise,name='cruise'),
    path('cruise-detail/<int:id>/',cruise_detail,name='cruise_detail'),
]