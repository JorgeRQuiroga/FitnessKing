from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('productos/', listar_productos, name="listarProductos"),
]
