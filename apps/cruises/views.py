from django.shortcuts import render
from apps.settings.models import Setting
from .models import Cruises

# Create your views here.
def cruise(request):
    setting = Setting.objects.latest('id')
    cruises = Cruises.objects.all()

    context = {
        'setting' : setting,
        'cruises' : cruises,
    }
    return render(request,'cruises.html',context)

def cruise_detail(request,id):
    setting = Setting.objects.latest('id')
    cruise = Cruises.objects.get(id=id)

    context = {
        'setting' : setting,
        'cruise' : cruise,
    }
    return render(request,'cruise_detail.html',context)