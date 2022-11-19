from django.shortcuts import render
from apps.settings.models import Setting
from .models import Hotels
# Create your views here.
def hotel_details(request, id):
    setting = Setting.objects.latest('id')
    hotel = Hotels.objects.get(id=id)
    context = {
        'setting' : setting,
        'hotel' : hotel,
    }
    return render(request,'booking/hotel.html', context)