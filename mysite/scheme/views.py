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


def single_scheme(request, pk):
    schema = Scheme.objects.get(pk=pk)
    row1 = [schema.order1, schema.name1, schema.type1]
    row2 = [schema.order2, schema.name2, schema.type2]
    row3 = [schema.order3, schema.name3, schema.type3]
    row4 = [schema.order4, schema.name4, schema.type4]
    row5 = [schema.order5, schema.name5, schema.type5]
    row6 = [schema.order6, schema.name6, schema.type6]
    #return render(request, "scheme/single_scheme.html", {"s": schema})
    return render(request, "scheme/single.html", {"s": schema, 'row1':row1, 'row2':row2, 'row3':row3, 'row4':row4, 'row5':row5, 'row6':row6})