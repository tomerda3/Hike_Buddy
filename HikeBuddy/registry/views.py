# from django.shortcuts import render, redirect
# from .forms import RegisterForm

# from django.contrib.auth.models import Group

# Create your views here.
# def signup(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             user = form.save()
#             Group.objects.get_or_create(name=form.cleaned_data['userType'])
#             cur_group = Group.objects.get(name=form.cleaned_data['userType'])
#             cur_group.user_set.add(user)

#             user.username = form.cleaned_data['username']
#             user.userType = form.cleaned_data['userType']
#             user.email = form.cleaned_data['email']
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.phone = form.cleaned_data['phone']

#             user.save()

#             return redirect("/login/")
#     else:
#         form = RegisterForm()
#     return render(response, "registry/signup.html", {"form":form})






from django.shortcuts import render, redirect
from .forms import UserProfileInfoForm, UserForm
from django.contrib.auth.models import Group
# from django import forms


def signup(response):
    registered = False

    if response.method == "POST":
        user_form = UserForm(data=response.POST)
        profile_form = UserProfileInfoForm(data=response.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            Group.objects.get_or_create(name=profile_form.cleaned_data['userType'])
            cur_group = Group.objects.get(name=profile_form.cleaned_data['userType'])
            cur_group.user_set.add(user)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.phone = profile_form.cleaned_data['phone']
            profile.save()
            print(profile.phone)


            if 'picture' in response.FILES:
                profile.profile_pic = response.FILES['picture']

            profile.save()

            registered = True
            return redirect("/login/")

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(response, "registry/signup.html",
        {'user_form':user_form,
        'profile_form':profile_form, 'registered':registered})