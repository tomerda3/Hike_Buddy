from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def profile(response):
    return render(response, "main/profile.html", {})


def toggle_active(response):
    user = User.objects.get(pk=response.user.id)
    user.is_active = not user.is_active
    user.save()
    redirect("/")
    return render(response, "main/home.html", {})


def feedback(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',
		 message,
		 settings.EMAIL_HOST_USER,
		 ['HikeBuddy100@gmail.com'],
		 fail_silently=False)
	return render(request, 'main/thankyou.html')

def about(response):
    return render(response, "main/about.html", {})

def contact(response):
    # return render(response, "main/contact.html", {})
    print("CONTACT")
    return render(response, "main/contact.html", {})