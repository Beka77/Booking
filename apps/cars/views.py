from django.shortcuts import render
from apps.settings.models import Setting
from .models import Car
from apps.settings.models import Currency

# Create your views here.
def car(request):
    setting = Setting.objects.latest('id')
    cars = Car.objects.all()
    currency = Currency.objects.all()
    context = {
        'setting' : setting,
        'cars' : cars,
        'currency' : currency
    }
    return render(request,'car_rentals.html',context)