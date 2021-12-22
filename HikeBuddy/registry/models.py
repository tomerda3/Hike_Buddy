from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional:
    userType = forms.CharField(label='User type', max_length=10, required=True)
    phone = models.CharField(max_length=10, default=None,)
    # picture = models.ImageField(upload_to='main\\templates\\main\\profile_pics', blank=True)
    picture = models.ImageField(upload_to='main\\media\\profile_pics', blank=True)

    def __str__(self):
        return self.user.username