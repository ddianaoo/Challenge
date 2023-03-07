from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied


def index(request):
    return HttpResponse('Hello')


def signin(request):
    return render(request, 'user/signin.html')