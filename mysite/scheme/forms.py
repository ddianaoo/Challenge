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