from django.shortcuts import render
from apps.settings.views import Setting
from .models import Locations
from apps.settings.models import Currency

# Create your views here.
def locations_detail(request, id):
    locations = Locations.objects.get(id = id).order_by("?")
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    context= {
        'locations' : locations,
        'setting': setting,
        'currency' : currency
    }
    return render (request, 'location.html', context)