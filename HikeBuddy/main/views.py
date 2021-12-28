from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import HostForm

# Create your views here.
from registry.models import UserProfileInfo

from .models import HostingPlace


def getUserProfileInfo(usr):
        upi = UserProfileInfo.objects.get(user=usr)
        return upi

def home(response):
    return render(response, "main/home.html", {})


def profile(response):
    public_ip = get_public_ip()
    loc = get_loc(public_ip)
    phone = UserProfileInfo.objects.get(user=response.user).phone
    picture = UserProfileInfo.objects.get(user=response.user).picture
    group = response.user.groups.get(user=response.user)
    hosting_places = None
    hosting_places_names = []
    if group.name == 'host':
        hosting_places = HostingPlace.objects.filter(username = response.user.username)

    if hosting_places:
        for hp in hosting_places:
            hosting_places_names.append(hp.name)

    return render(response, "main/profile.html", {
        'ip': public_ip,
        'loc': loc,
        'phone': phone,
        'profile_pic': picture,
        'hosting_places': str(hosting_places_names)[1:-1:],
        'hosting_places_len': len(hosting_places_names),
        })


def toggle_active(response):
    user = User.objects.get(pk=response.user.id)
    user.is_active = not user.is_active
    user.save()
    redirect("/")
    return render(response, "main/home.html", {})


def feedback(response):
	if response.method == 'POST':
		message = response.POST['message']
		send_mail('Contact Form',
		 message,
		 settings.EMAIL_HOST_USER,
		 ['HikeBuddy100@gmail.com'],
		 fail_silently=False)
	return render(response, 'main/thankyou.html')

def about(response):
    return render(response, "main/about.html", {})

def contact(response):
    return render(response, "main/contact.html", {})

def planroute(response):
    return render(response, "main/planroute.html", {})

def areyousure(response):
    return render(response, "main/areyousure.html", {})

def get_public_ip():
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip

def get_loc(ip):
    import geoip2.database
    reader = geoip2.database.Reader('./GeoLite2-City_20190430/GeoLite2-City.mmdb')
    response = reader.city(ip)
    # print(response.country.iso_code)
    # print(response.country.name)
    # print(response.country.names['zh-CN'])
    # print(response.subdivisions.most_specific.name)
    # print(response.subdivisions.most_specific.iso_code)
    # print(response.city.name)
    # print(response.postal.code)
    # print(response.location.latitude)
    # print(response.location.longitude)
    return response.country.name

def creathostingplaces(response):
    form = HostForm()
    return render(response, "main/creathostingplaces.html", {"form":form})

def myhostingplaces(response):
    form = HostForm()
    return render(response, "main/myhostingplaces.html", {"form":form})

def createHost(response):
    if response.method == "POST":
        form = HostForm(response.POST)

        if form.is_valid():
            form.name = form.cleaned_data["name"]
            form.location = form.cleaned_data["location"]

            hp = HostingPlace(name=form.name)
            hp.location = form.location
            hp.fireplace = form.cleaned_data["fireplace"]
            hp.singleBeds = form.cleaned_data["singleBeds"]
            hp.doubleBeds = form.cleaned_data["doubleBeds"]
            hp.freeWiFi = form.cleaned_data["freeWiFi"]
            hp.showers = form.cleaned_data["showers"]
            hp.electricity = form.cleaned_data["electricity"]
            hp.breakfast = form.cleaned_data["breakfast"]
            hp.airConditioning = form.cleaned_data["airConditioning"]
            hp.parking = form.cleaned_data["parking"]
            hp.bar = form.cleaned_data["bar"]
            hp.username = response.user.username
            hp.save()

            return home(response)

    else:
        form = HostForm()

    return render(response, "main/myhostingplaces.html", {"form":form})