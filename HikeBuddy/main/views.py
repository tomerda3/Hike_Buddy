from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from registry.models import UserProfileInfo
def home(response):
    return render(response, "main/home.html", {})


def profile(response):
    public_ip = get_public_ip()
    loc = get_loc(public_ip)
    phone = UserProfileInfo.objects.get(user=response.user).phone
    return render(response, "main/profile.html", {'ip': public_ip, 'loc': loc, 'phone':phone})


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