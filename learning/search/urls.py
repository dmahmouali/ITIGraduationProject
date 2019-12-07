from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/<searchkey>/' , views.index, name='index'),
    
]
