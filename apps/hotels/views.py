from django.shortcuts import render
from apps.settings.models import Setting
from .models import Hotels, Currency
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

    return render(request,'hotel.html', context)