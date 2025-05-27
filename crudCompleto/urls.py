from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('', listar_productos, name="listarProductos"),
]
