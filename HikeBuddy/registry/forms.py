from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    USER_TYPES = [('traveler', 'Traveler'),
    ('guide', 'Guide'),
    ('host', 'Host'),]
    userType = forms.CharField(label='User type', widget=forms.Select(choices=USER_TYPES))
    phone = forms.CharField(label='Phone number', max_length=10, required=False)

    
    class Meta:
        model = User
        fields = [
        "username",
        "first_name",
        "last_name",
        "userType",
        "email",
        "phone",
        "password1",
        "password2"
        ]