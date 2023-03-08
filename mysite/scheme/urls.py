from django.urls import path
from .views import *


urlpatterns = [
    path('all/', get_schemas, name='schemas'),
    path('add/', add_scheme, name='add_scheme'),
]