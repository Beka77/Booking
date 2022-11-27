from django.shortcuts import render
from apps.settings.models import Setting
from .models import Hotels, Currency, HotelImage
# Create your views here.
def hotel(request, id):
    setting = Setting.objects.latest('id')
    hotel = Hotels.objects.get(id=id)
    currency = Currency.objects.all()
    context = {
        'setting' : setting,
        'hotel' : hotel,
        'currency' : currency
    }

    return render(request,'hotels.html', context)

def hotel_details(request, id):
    setting = Setting.objects.latest('id')
    hotel = Hotels.objects.get(id=id)
    motels = Hotels.objects.order_by('?')
    hotel_images = HotelImage.objects.all().filter(hotel = hotel)
    context = {
        'setting' : setting,
        'hotel' : hotel,
        'hotel_images' : hotel_images,
        'motels' : motels,
    }
    return render(request,'hotel.html', context)









def all_hotels(request):
    setting = Setting.objects.latest('id')
    hotels = Hotels.objects.all()
    context = {
        'setting' : setting,
        'hotels' : hotels,
    }
    return render(request,'hotels.html', context)