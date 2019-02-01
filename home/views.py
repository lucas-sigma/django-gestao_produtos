from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'home.html')

def signup(request):
    pass

def logout(request):
    logout(request)

    return redirect(home)

def login(request):
    pass