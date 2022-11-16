from django.shortcuts import render
from apps.settings.models import Setting
from apps.hotels.models import Hotels
from apps.settings.models import Currency
from apps.locations.models import Locations
from apps.users.models import User
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all().order_by("?")
    currency = Currency.objects.all()
    users = User.objects.all()
    context = {
        'setting' : setting,
        'locations' : locations,
        'currency' : currency,
        'users' : users,
    }
    return render (request, 'index.html', context) 