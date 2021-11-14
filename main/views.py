from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages

# Custom objects
from .models import Service
from .forms import ServiceForm, CreateUserForm
from .filters import ServiceFilter

# Users imports
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Pagination imports
from django.core.paginator import Paginator


# SERVICES

@login_required(login_url='login')
def index(request):
    services = Service.objects.all().order_by('-datecreated')

    myFilter = ServiceFilter(request.GET, queryset=services)
    services = myFilter.qs

    p = Paginator(myFilter.qs, 3)
    page = request.GET.get('page')
    services = p.get_page(page)

    return render(request, 'index.html', {'services': services, 'myFilter': myFilter})


@login_required(login_url='login')
def view_service(request, pk):
    services = Service.objects.get(id=pk)
    return render(request, 'view_service.html', {'services': services})


@login_required(login_url='login')
def create(request):
    form = ServiceForm()

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


@login_required(login_url='login')
def update(request, pk):

    service = Service.objects.get(id=pk)

    if request.user == service.author:
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
    else:
        return redirect('/')


@login_required(login_url='login')
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
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

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


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    
    form = CreateUserForm(instance=request.user)
    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account have been updated')

            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)
