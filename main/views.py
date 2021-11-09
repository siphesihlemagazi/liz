from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm 

from django.contrib.auth.models import User, auth
from django.contrib import messages

from .filters import ServiceFilter


from django.contrib.auth.decorators import login_required

# PAGINATION STUFF
from django.core.paginator import Paginator

# SERVICES

@login_required(login_url='login')
def index(request):
    services = Service.objects.all()

    myFilter = ServiceFilter(request.GET, queryset = services)
    services = myFilter.qs

    p = Paginator(myFilter.qs, 2)
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

            elif len(password) < 7:
                messages.info(request, 'Password too short')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password didn't match")
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


def logout(request):
    auth.logout(request)
    return redirect('login')


