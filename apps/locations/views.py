from django.shortcuts import render
from apps.settings.views import Setting
from .models import Locations
# Create your views here.
def locations_detail(request, id):
    locations = Locations.objects.get(id = id).order_by("?")
    setting = Setting.objects.latest('id')
    context= {
        'locations' : locations,
        'setting': setting,
    }
    return render (request, 'location.html', context)