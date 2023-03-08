from django.shortcuts import render, redirect
from .models import *
from .forms import SchemeForm
from django.http import HttpResponse
from django.views.generic import ListView


def get_schemas(request):
    user = request.user
    queryset = Scheme.objects.filter(user=user)
    return render(request, "scheme/get_schemas.html", {"object_list": queryset})


def add_scheme(request):
    #return render(request, 'scheme/add_scheme.html')

    user = request.user
    user = user.id
    success_url = '/all'

    if request.method == 'POST':
        form = SchemeForm(request.POST, initial={'user': user})
        if form.is_valid():
            form.save()
            return redirect('schemas')

    return render(request, 'scheme/add_scheme.html', {'form': SchemeForm(initial={'user': user}), })


