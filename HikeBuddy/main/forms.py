from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import HostingPlace
from .models import GuideInfo


class HostForm(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    fireplace = forms.BooleanField(required=False, initial=False, label="Fireplace")
    singleBeds = forms.BooleanField(required=False, initial=False, label="Single Beds")
    doubleBeds = forms.BooleanField(required=False, initial=False, label="Double Beds")
    freeWiFi = forms.BooleanField(required=False, initial=False, label="Free WiFi")
    showers = forms.BooleanField(required=False, initial=False, label="Showers")
    electricity = forms.BooleanField(required=False, initial=False, label="Electricity")
    breakfast = forms.BooleanField(required=False, initial=False, label="Breakfast")
    airConditioning = forms.BooleanField(required=False, initial=False, label="Air Conditioning")
    parking = forms.BooleanField(required=False, initial=False, label="Parking")
    bar = forms.BooleanField(required=False, initial=False, label="Bar")

    class Meta:
        model = HostingPlace
        fields=(
            'name',
            'location',
            'fireplace',
            'singleBeds',
            'doubleBeds',
            'freeWiFi',
            'showers',
            'electricity',
            'breakfast',
            'airConditioning',
            'parking',
            'bar',
            )
###############################
class GuideForm(forms.Form):
    cost = forms.FloatField(required=True)
    carryweapon = forms.BooleanField(required=False, initial=False, label="Carry Weapon")
    medic = forms.BooleanField(required=False, initial=False, label="Medic")
    transportationvehicle = forms.BooleanField(required=False, initial=False, label="Transportation Vehicle")

    class Meta:
        model = GuideInfo
        fields=(
            'cost',
            'carryweapon',
            'medic',
            'transportationvehicle',
            )