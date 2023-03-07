from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    # path('remove/<int:pk>/', remove_author, name='remove_author'),
]