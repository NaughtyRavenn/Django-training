from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import logout


def index(request):
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")


def error(request, exception):
    return render(request, "pages/error.html")


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, "pages/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
