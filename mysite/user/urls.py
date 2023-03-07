from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    # path('create/', create_author, name='create_author'),
    # path('remove/<int:pk>/', remove_author, name='remove_author'),
]