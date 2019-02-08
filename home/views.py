from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('estoque')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form':form})

def my_logout(request):
    logout(request)

    return redirect('home')