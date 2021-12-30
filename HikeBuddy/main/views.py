from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import HostForm
from .forms import GuideForm
import os
from django.contrib.auth.models import Group
from registry.models import UserProfileInfo
from .models import HostingPlace, GuideInfo

from .filters import HostingPlaceFilter

# Create your views here.

def getUserProfileInfo(usr):
        upi = UserProfileInfo.objects.get(user=usr)
        return upi

def home(response):
    return render(response, "main/home.html", {})


def myprofile(response):
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

    guideinfo = None
    if group.name == 'guide':
        guideinfo = GuideInfo.objects.filter(username = response.user.username)
        if str(guideinfo)!="<QuerySet []>": guideinfo=guideinfo[0]

    return render(response, "main/myprofile.html", {
        'ip': public_ip,
        'loc': loc,
        'phone': phone,
        'profile_pic': picture,
        'hosting_places': str(hosting_places_names)[1:-1:],
        'hosting_places_len': len(hosting_places_names),
        'guideinfo': guideinfo,
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
    path="static\\trails"
    trails = os.listdir(path)
    trail_data = []
    public_ip = get_public_ip()
    loc = get_loc(public_ip)
    for trail in trails:
        trail_data.append([])
        f = open('static\\trails\\'+trail, 'r')
        if f.mode == 'r':
            content = f.read()
            content = content.split('\n')
            for line in content:
                trail_data[-1].append(line)
    guideinfo = None
    guide_routes = None
    show = True

    group = response.user.groups.get(user=response.user)
    if group.name == 'guide':
        guideinfo = GuideInfo.objects.filter(username = response.user.username)
        if str(guideinfo)!="<QuerySet []>":
            guideinfo=guideinfo[0]
        else:
            show = False
    if guideinfo: guide_routes = guideinfo.routes

    return render(response, "main/planroute.html", {
        'loc': loc,
        'trails': trail_data,
        'guide_routes': guide_routes,
        'show': show
        })

def addroute(response, route):
    guide = GuideInfo.objects.filter(username = response.user.username)
    if str(guide)!="<QuerySet []>":
        guide=guide[0]
        print(guide.routes)
        if guide.routes == 'None':
            guide.routes = str(route)
        else:
            if str(route) not in guide.routes:
                guide.routes += ', ' + str(route)
            else:  # delete route
                if guide.routes == route:  # single route
                    guide.routes = 'None'
                else:  # multiple routes
                    string1 = ", "+route+", "
                    string2 = route+", "
                    string3 = ", "+route
                    if string1 in guide.routes:
                        guide.routes = guide.routes.replace(string1, ", ")
                    elif string2 in guide.routes:
                        guide.routes = guide.routes.replace(string2, "")
                    elif string3 in guide.routes:
                        guide.routes = guide.routes.replace(string3, "")
                if guide.routes == '': guide.routes = 'None'
        guide.save()
    return planroute(response)

def findhost(response):
    order_by = response.GET.get('order_by', 'id')
    hosting_places = HostingPlace.objects.all().order_by(order_by)

    myFilter = HostingPlaceFilter(response.GET, queryset=hosting_places)
    hosting_places = myFilter.qs

    return render(response, "main/findhost.html", {
        'hosting_places': hosting_places,
        'myFilter': myFilter,
        })

def findguide(response):
    order_by = response.GET.get('order_by', 'id')
    guides = GuideInfo.objects.all().order_by(order_by)
    profiles = UserProfileInfo.objects.filter()
    return render(response, "main/findguide.html", {
        'guides': guides,
        'profiles': profiles,
        })

def profile(response, username):
    hostuser = User.objects.get(username = username)
    hostprofileinfo = (UserProfileInfo.objects.filter(user = hostuser))[0]
    hosting_places = HostingPlace.objects.filter(username = hostuser.username)
    hosting_places_names = []
    picture = hostprofileinfo.picture
    if picture: picture = picture.path

    if hosting_places:
        for hp in hosting_places:
            hosting_places_names.append(hp.name)

    guideinfo = None
    guide_routes = None
    group = Group.objects.get(name='guide')
    try:
        guide = group.user_set.get(username=username)
    except:
        guide = None
    if group.name == 'guide':
        try:
            guideinfo = GuideInfo.objects.get(username=username)
        except:
            guideinfo = None
        print(guideinfo)
    #     if str(guideinfo)!="<QuerySet []>": guideinfo=guideinfo[0]

    return render(response, "main/profile.html", {
        'hostprofileinfo': hostprofileinfo,
        'hostuser': hostuser,
        'hosting_places': str(hosting_places_names)[1:-1:],
        'hosting_places_len': len(hosting_places_names),
        'profile_pic': picture,
        'guideinfo': guideinfo,
        })

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

def createhostingplace(response):
    form = HostForm()
    return render(response, "main/createhostingplace.html", {"form":form})

def myhostingplaces(response):
    group = response.user.groups.get(user=response.user)
    hosting_places = None
    if group.name == 'host':
        hosting_places = HostingPlace.objects.filter(username = response.user.username)
    return render(response, "main/myhostingplaces.html", {
        'hosting_places': hosting_places,
        })

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

def guideinfo(response):
    form = GuideForm()
    
    show = True
    group = response.user.groups.get(user=response.user)    
    if group.name == 'guide':
        guideinfo = GuideInfo.objects.filter(username = response.user.username)
        if str(guideinfo) != "<QuerySet []>": show = False

    return render(response, "main/guide.html", {"form":form, "show": show})

def createGuide(response):
    if response.method == "POST":
        form = GuideForm(response.POST)
        if form.is_valid():
            print("valid")
            form.cost = form.cleaned_data["cost"]

            cg = GuideInfo()
            cg.username = response.user.username
            cg.cost = form.cost
            cg.carryweapon = form.cleaned_data["carryweapon"]
            cg.medic = form.cleaned_data["medic"]
            cg.transportationvehicle = form.cleaned_data["transportationvehicle"]
            cg.routes = 'None'
            cg.save()

            return myprofile(response)
        else: print(form.errors)

    else:
        form = GuideForm()

    return myprofile(response)
    # return render(response, "main/home.html", {"form":form})