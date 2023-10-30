from django.urls import path
from app1 import views

urlpatterns = [
    path("" , views.index),
    path("elements/" , views.elements, name="elements"),
    path("generic/" , views.generic , name="generic")
]
