from django.shortcuts import render, redirect
from .models import *
from .forms import SchemeForm
from django.http import HttpResponse
from django.views.generic import ListView
import datetime
from .tasks import datagenerate
from django.core.exceptions import PermissionDenied


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
            print('okey')
            form.save()
            return redirect('schemas')
        print(form.errors)
        print('neokey')
    # scheme_form
    return render(request, 'scheme/add_scheme.html', {'form': SchemeForm(initial={'user': user}), })


def delete_scheme(request, pk):
    schema = Scheme.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == schema.user:
        schema.delete()

    return redirect('schemas')


def single_generate(request, pk):
    scheme = Scheme.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == scheme.user:

        if request.method == 'POST':
            rows = int(request.POST['rows'])

            columns = []

            columns.append(scheme.type1)
            columns.append(scheme.type2)
            columns.append(scheme.type3)
            columns.append(scheme.type4)
            columns.append(scheme.type5)
            columns.append(scheme.type6)

            col_names = (
            ('0', 'Choose..'),
            ('1', 'Full Name'),
            ('2', 'Job'),
            ('3', 'Company'),
            ('4', 'Integer'),
            ('5', 'Text'),
            ('6', 'Email'),
            )

            def replace(list, dictionary):
                for idx, val in enumerate(list):
                    list[idx] = dictionary[int(list[idx])]
                return list

            replace(columns, col_names)
            columns_real = [i[1] for i in columns]
            while 'Choose..' in columns_real:
                columns_real.remove('Choose..')

            names = []

            names.append(scheme.name1)
            names.append(scheme.name2)
            names.append(scheme.name3)
            names.append(scheme.name4)
            names.append(scheme.name5)
            names.append(scheme.name6)

            while '' in names:
                names.remove('')

            while 'Column' in names:
                names.remove('Column')

            order = []

            order.append(scheme.order1)
            order.append(scheme.order2)
            order.append(scheme.order3)
            order.append(scheme.order4)
            order.append(scheme.order5)
            order.append(scheme.order6)

            while 0 in order:
                order.remove(0)

            if order:
                columns_real = [x for _, x in sorted(zip(order, columns_real))]
                names = [x for _, x in sorted(zip(order, names))]

            filename = 'media/' + str(scheme.user) + '_' + str(scheme.name) + '_' + str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

            task = datagenerate(rows, columns_real, names, filename, pk)
            return redirect('single_scheme', pk=pk)

        schema = Scheme.objects.get(pk=pk)
        row1 = [schema.order1, schema.name1, schema.type1]
        row2 = [schema.order2, schema.name2, schema.type2]
        row3 = [schema.order3, schema.name3, schema.type3]
        row4 = [schema.order4, schema.name4, schema.type4]
        row5 = [schema.order5, schema.name5, schema.type5]
        row6 = [schema.order6, schema.name6, schema.type6]
        rows = [row1, row2, row3, row4, row5, row6]
        rows.sort(key=lambda x: x[0])

        queryset = DataSets.objects.filter(scheme=pk).order_by('-id')
        return render(request, "scheme/single_generate.html", {"s": schema, 'rows': rows, 'pk': pk, 'queryset': queryset})
    raise PermissionDenied