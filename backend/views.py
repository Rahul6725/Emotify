from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, "welcome.html")

def login(request): 
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

def account(request):
    return render(request, "account.html")