from django.urls import path, include
from agregar_producto import views

urlpatterns = [
    path('', views.agregar_producto, name='agregar_producto'),
]
