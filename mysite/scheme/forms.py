from django import forms
from .models import *


class SchemeForm(forms.ModelForm):

    class Meta:
        model = Scheme
        fields = ['name', 'user',
                  'type1', 'type2', 'type3', 'type4', 'type5', 'type6',
                  'name1', 'name2', 'name3', 'name4', 'name5', 'name6',
                  'order1', 'order2', 'order3', 'order4', 'order5', 'order6',
                  'rows']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name1': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name2': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name3': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name4': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name5': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'name6': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'type1': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'type2': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'type3': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'type4': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'type5': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'type6': forms.Select(attrs={'class': 'form-select', 'style': 'width:300px'}),
            'order1': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'order2': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'order3': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'order4': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'order5': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'order6': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
        }
        labels = {
            'name':  'Name',
            'name1': 'Column name',
            'name2': 'Column name',
            'name3': 'Column name',
            'name4': 'Column name',
            'name5': 'Column name',
            'name6': 'Column name',
            'type1': 'Type',
            'type2': 'Type',
            'type3': 'Type',
            'type4': 'Type',
            'type5': 'Type',
            'type6': 'Type',
            'order1': 'Order',
            'order2': 'Order',
            'order3': 'Order',
            'order4': 'Order',
            'order5': 'Order',
            'order6': 'Order',
        }
        choices = {
            'type1': CHOICES,
            'type2': CHOICES,
            'type3': CHOICES,
            'type4': CHOICES,
            'type5': CHOICES,
            'type6': CHOICES,

        }