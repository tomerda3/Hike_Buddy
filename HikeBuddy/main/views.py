from django.shortcuts import render
# from django.http import HttpResponse
# from .models import ToDoList, Item
# Create your views here.

# def index(response):
#     return HttpResponse("<center><h1>Main</h1></center>")

def home(response):
    return render(response, "main/home.html", {})

# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     return render(response, "main/base.html", {})

# def index(response, name):
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.get(id=1)
#     return HttpResponse("<center><h1>%s</h1><p>%s</p></center>" %(ls.name, str(item.text)))