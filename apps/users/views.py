from django.shortcuts import render, redirect
from apps.settings.models import Setting
from .models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from apps.locations.models import Locations
# Create your views here.

def register(request ):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all().order_by("?")
    context = {
        'setting' : setting,
        'locations' : locations
    }
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, phone = phone,)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request, 'register.html', context)

def login(request):
    setting = Setting.objects.latest('id')
    locations = Locations.objects.all().order_by("?")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('error.html')
    context = {
        'setting' : setting,
        'locations' : locations

    }
    return render(request, 'login.html', context)


def account(request, username):
    setting = Setting.objects.all()
    user = User.objects.get(username = username)
    context = {
        'user' : user,
        'setting' : setting,
    }
    return render(request, 'my_account.html', context) 


def account_update(request, id):
    user = User.objects.get(id = id)
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user = User.objects.get(id = id)
            user.username = username 
            user.first_name = first_name
            user.last_name = last_name
            user.email = email 
            user.phone = phone 
            user.save()
            return redirect('account', user.username)
        if 'delete' in request.POST:
            user = User.objects.get(id = id)
            user.delete()
            return redirect('index')
        if 'update_password' in request.POST:
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username = request.user)
                    if user.check_password(password):
                        user.set_password(new_password)
                        user.save()
                        return redirect('index', user.username)
                    else:
                        return HttpResponse("Текущий пароль не верный")
                except:
                    return HttpResponse("Пользователь не найден")
            else:
                return HttpResponse("Пароли различаются")
    context = {
        'user' : user,
        'setting' : setting,
    }
    return render(request, 'page-account-edit.html', context)

