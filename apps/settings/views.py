from django.shortcuts import render, redirect
from apps.settings.models import Setting, Contact
from apps.hotels.models import Hotels
from apps.settings.models import Currency
from apps.locations.models import Locations
from apps.users.models import User
from django.core.mail import send_mail

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all().order_by("?")
    currency = Currency.objects.all()
    users = User.objects.all()
    hotels = Hotels.objects.all()
    context = {
        'setting' : setting,
        'locations' : locations,
        'currency' : currency,
        'users' : users,
        'hotels' : hotels,
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