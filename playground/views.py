from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Userlevels
# Create your views here.


def view_login_page(request):
    return render(request,"login.html")  

def form(request):
    if request.method=="POST":
        username= request.POST["username"]
        pass1=request.POST["pass1"]
       #user=authenticate(username=username,password=pass1)
        user_level = Userlevels.objects.filter(username = username); 
        return render(request,"form.html", {'level': user_level}) 


    