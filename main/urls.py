from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('habesha-shopping-center/' , views.hsc),
    path('ethio-cloud-computing-systems/' , views.eccs)
]


