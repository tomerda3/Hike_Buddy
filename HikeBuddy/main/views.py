from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def profile(response):
    return render(response, "main/profile.html", {})


def toggle_active(response):
    user = User.objects.get(pk=response.user.id)
    user.is_active = not user.is_active
    user.save()
    redirect("/")
    return render(response, "main/home.html", {})

