from django.urls import path,include

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("profile/", views.profile, name="profile"),
path("contact/", views.contact, name="contact"),
path("about/", views.about, name="about"),
path("areyousure/", views.areyousure, name="areyousure"),
path("planroute/", views.planroute, name="planroute"),
path("findhost/", views.findhost, name="findhost"),
path("myhostingplaces/", views.myhostingplaces, name="myhostingplaces"),
path("createhostingplace/", views.createhostingplace, name="createhostingplace"),
path("createHost/", views.createHost, name="createHost"),
path("guideinfo/", views.guideinfo, name="guideinfo"),
path("createGuide/", views.createGuide, name="createGuide"),
path("host/<hostprofile>", views.host, name="host"),
]