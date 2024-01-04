from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def registration(response):
    form = RegisterForm()  # Instantiate the form
    return render(response, "register.html", {"form": form})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})
def landing_page(request):
    return render(request, 'base.html')
@login_required
def dashboard(response):
    return render(response, 'dashboard.html')