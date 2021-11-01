from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm  # ,CreateUserForm
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User, auth
from django.contrib import messages


# SERVICES

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})


def view_service(request, pk):
    services = Service.objects.get(id=pk)
    return render(request, 'view_service.html', {'services': services})


def create(request):
    form = ServiceForm()

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def update(request, pk):

    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def delete(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()  # if delete ever has a bug it that i have a function by its name
        return redirect('/')
    context = {
        'service': service
    }
    return render(request, 'delete.html', context)


# USERS

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# def register(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#         # return redirect('/')

#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)


# def login(request):
#     context = {

#     }
#     return render(request, 'login.html', context)
