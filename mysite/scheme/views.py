from django.shortcuts import render, redirect
from .models import *
from .forms import SchemeForm
from django.http import HttpResponse
from django.views.generic import ListView


def get_schemas(request):
    if request.user.is_authenticated:
        user = request.user
        queryset = Scheme.objects.filter(user=user).order_by('-id')
        return render(request, "scheme/get_schemas.html", {"object_list": queryset})
    return redirect('signin')


def add_scheme(request):
    user = request.user
    user = user.id
    if request.method == 'POST':
        form = SchemeForm(request.POST, initial={'user': user})
        if form.is_valid():
            form.save()
            return redirect('schemas')
    # scheme_form
    return render(request, 'scheme/add_scheme.html', {'form': SchemeForm(initial={'user': user}), })


def delete_scheme(request, pk):
    schema = Scheme.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == schema.user:
        schema.delete()

    return redirect('schemas')

