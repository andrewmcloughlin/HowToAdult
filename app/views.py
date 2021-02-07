
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from .models import *
from .forms import *
#from .filters import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if  request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created for ' + user)
                return redirect('login')
        context= {
            'form': form
        }
        return render(request, 'HowToAdult/register.html', context)

def loginPage(request):
    if  request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('Policy_table')
            else:
                messages.info(request,'Username or password is incorrect.')
        context= {}
        return render(request, 'HowToAdult/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    

@login_required(login_url='login')
def Policy_table(request):
    all_objects = Policy.objects.all()
    context = {'all_objects': all_objects,}
    return render(request, 'Policy/table.html', context)

@login_required(login_url='login')
def Policy_map(request):
    all_objects = Policy.objects.all()
    context = {'all_objects': all_objects,}
    return render(request, 'Policy/map.html', context)

@login_required(login_url='login')
def Category_calendar(request):
    all_objects = Category.objects.all()
    context = {'all_objects': all_objects,}
    return render(request, 'Category/calendar.html', context)

@login_required(login_url='login')
def Category_images(request):
    all_objects = Category.objects.all()
    context = {'all_objects': all_objects,}
    return render(request, 'Category/images.html', context)
@login_required(login_url='login')
def add_Policy(request):
    form = PolicyForm()
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PolicyForm()
            return redirect('Policy_table')
    context = {'form': form}
    return render(request, 'HowToAdult/add_Policy.html', context)

@login_required(login_url='login')
def update_Policy(request, id):
    instance = Policy.objects.get(id=id)
    form = PolicyForm(instance=instance)
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            form = PolicyForm()
            return redirect('Policy_table')
    context = {'form': form}
    return render(request, 'HowToAdult/add_Policy.html', context)

@login_required(login_url='login')
def delete_Policy(request, id):
    instance = Policy.objects.get(id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('Policy_table')
    context = {'item':instance}
    return render(request, 'HowToAdult/delete_Policy.html', context)

@login_required(login_url='login')
def add_Category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CategoryForm()
            return redirect('Policy_table')
    context = {'form': form}
    return render(request, 'HowToAdult/add_Category.html', context)

@login_required(login_url='login')
def update_Category(request, id):
    instance = Category.objects.get(id=id)
    form = CategoryForm(instance=instance)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            form = CategoryForm()
            return redirect('Policy_table')
    context = {'form': form}
    return render(request, 'HowToAdult/add_Category.html', context)

@login_required(login_url='login')
def delete_Category(request, id):
    instance = Category.objects.get(id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('Policy_table')
    context = {'item':instance}
    return render(request, 'HowToAdult/delete_Category.html', context)

