from django.urls import path,include

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("contact/", views.contact, name="contact"),
path("about/", views.about, name="about"),
path("areyousure/", views.areyousure, name="areyousure"),
path("planroute/", views.planroute, name="planroute"),
path("findhost/", views.findhost, name="findhost"),
path("findguide/", views.findguide, name="findguide"),
path("myhostingplaces/", views.myhostingplaces, name="myhostingplaces"),
path("createhostingplace/", views.createhostingplace, name="createhostingplace"),
path("createHost/", views.createHost, name="createHost"),
path("guideinfo/", views.guideinfo, name="guideinfo"),
path("createGuide/", views.createGuide, name="createGuide"),
path("profile/<username>", views.profile, name="profile"),
path("profile/", views.myprofile, name="myprofile"),
path("addroute/<route>", views.addroute, name="addroute"),
]