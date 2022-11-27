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

def car_detail(request,id):
    setting = Setting.objects.latest('id')
    car = Car.objects.get(id = id)
    
    context = {
        'setting' : setting,
        'car' : car,
    }
    return render(request,'cars.html',context)