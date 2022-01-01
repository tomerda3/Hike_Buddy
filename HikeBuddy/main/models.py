from django.db import models
# from django.contrib.auth.models import User
# from registry.models import UserProfileInfo
from django import forms

# Create your models here.

class HostingPlace(models.Model):

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    fireplace = models.BooleanField(default=False)
    singleBeds = models.BooleanField(default=False)
    doubleBeds = models.BooleanField(default=False)
    freeWiFi = models.BooleanField(default=False)
    showers = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    airConditioning = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    username = models.CharField(max_length=200, default='')
    picture = models.ImageField(blank=True, upload_to='static\\media\\host_pics')



    def __str__(self):
        return self.name

class GuideInfo(models.Model):

    routes = models.CharField(max_length=1000, default='None')
    cost = models.FloatField(max_length=200)
    carryweapon = models.BooleanField(default=False)
    medic = models.BooleanField(default=False)
    transportationvehicle = models.BooleanField(default=False)
    username = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.username