from django.urls import path,include

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("profile/", views.profile, name="profile"),
path('contact/', views.contact, name="contact"),
path('about/', views.about, name="about"),

    # path("home/", views.home, name="home"),
# path("<str:name>", views.index, name="name"),
]