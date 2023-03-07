from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView


def get_schemas(request):
    return render(request, 'scheme/get_schemas.html')

def add_scheme(request):
    return render(request, 'scheme/add_scheme.html')


