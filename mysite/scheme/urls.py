from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('all/', login_required(get_schemas), name='schemas'),
    path('add/', login_required(add_scheme), name='add_scheme'),
    path('delete/<int:pk>/', login_required(delete_scheme), name='delete_scheme'),
    path('details/<int:pk>/', login_required(single_generate), name='single_scheme'),
]