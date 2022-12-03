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

    