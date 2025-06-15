from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'users/index.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, 'users/register.html', {"error": "Passwords do not match."})
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {"error": "Username already taken."})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('index')

    return render(request, 'users/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'users/login.html', {"error": "Invalid credentials"})
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
