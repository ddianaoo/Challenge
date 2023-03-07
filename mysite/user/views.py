from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


def index(request):
    return render(request, 'user/index.html', {'message': 'Hello'})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'user/signin.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('/')