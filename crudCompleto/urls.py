from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('productos/', listar_productos, name="listarProductos"),
    path('registrar/', registrar_producto, name="registrarProducto"),
    path('productos/<int:pk>/editar/', editar_producto, name="editarProducto"),
]
