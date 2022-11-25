from django.shortcuts import render, redirect
from apps.settings.models import Setting, Contact
from apps.hotels.models import Hotels
from apps.settings.models import Currency
from apps.locations.models import Locations
from apps.users.models import User
from apps.cars.models import Car
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all().order_by("?")
    currency = Currency.objects.all()
    users = User.objects.all()
    hotels = Hotels.objects.all()
    car = Car.objects.all()
    context = {
        'setting' : setting,
        'locations' : locations,
        'currency' : currency,
        'users' : users,
        'hotels' : hotels,
        'car' : car
    }
    return render (request, 'index.html', context) 

def thank_you(request):
    return render (request, 'thank_you.html')

def user_not_found(request):
    return render(request, 'user_not_found.html')

def register_error(request):
    return render(request, 'register_error.html')

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, email = email, message = message,)
        send_mail(
                    # title:
                    f"{setting.title}",
                    # message:
                    f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение: {message}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
        return redirect('thank_you')
    context = {
        'setting' : setting
    }
    return render (request, 'contact.html', context) 


def search(request):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all()
    car = Car.objects.all()
    search_key = request.POST.get('key')
    if search_key:
        locations = Locations.objects.filter(Q(title_icontains = search_key))
        car = Car.objects.filter(Q(title_icontains = search_key))
    context = {
        'setting' : setting,
        'locations' : locations,
        'car' : car,
    }
    return render(request, 'search_results.html', context)