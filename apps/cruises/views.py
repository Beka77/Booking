from django.shortcuts import render
from .models import Cruises, Currency
from apps.settings.views import Setting

# Create your views here.
def cruise(request):
    setting = Setting.objects.latest('id')
    cruises = Cruises.objects.all()
    currency = Currency.objects.all()
    context = {
        'setting' : setting,
        'cruises' : cruises,
        'currency' : currency
    }
    return render(request,'cruises.html',context)