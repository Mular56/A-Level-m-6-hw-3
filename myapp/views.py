from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PersonForm, RegistrationForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import MyUser


def search_comments(request):
    return render(request, 'search_comments.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been updated successfully!')
                return redirect('change_password')
            else:
                messages.error(request, 'Invalid old password.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def welcome(request):
    return render(request, 'welcome.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = None 
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_view')  
    else:
        form = LoginForm()  
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home_view')  


def check_eligibility(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            gender = cleaned_data['gender']
            age = cleaned_data['age']
            english_level = cleaned_data['english_level']
            
            if (gender == 'M' and age >= 20 and english_level in ['B2', 'C1', 'C2']) or \
               (gender == 'F' and age >= 22 and english_level in ['B2', 'C1', 'C2']):
                return HttpResponse('Ви підходитие!')
            else:
                return HttpResponse('Ви не підходитие!')
    else:
        form = PersonForm()
    return render(request, 'check_eligibility.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
