from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index),
    path("/elements" , views.elements),
    path("/generic/" , views.generic)
]