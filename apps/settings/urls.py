from xml.etree.ElementInclude import include
from django.urls import path 
from .views import index 
from apps.users.views import login
from apps.settings.views import contact, thank_you



urlpatterns = [
    path('', index, name = "index"),
    path('login/', login, name = "login"),
    path('contact/', contact, name = "contact"),
    path('thank_you/', thank_you, name = "thank_you"),
] 