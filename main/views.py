from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm


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
        service.delete() # if delete ever has a bug it that i have a function by its name
        return redirect('/')
    context = {
        'service': service
    }
    return render(request, 'delete.html', context)
