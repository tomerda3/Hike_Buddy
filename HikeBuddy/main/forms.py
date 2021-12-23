from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import HostingPlace


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
    picture = models.ImageField(upload_to='picture', blank=True)

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
            'picture')