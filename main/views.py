from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


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
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('/')
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    context = {

    }
    return render(request, 'login.html', context)
