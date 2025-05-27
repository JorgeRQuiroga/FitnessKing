from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('', listar_productos, name="listarProductos"),
    path('editar/1', editar_producto, name="editarProducto"),
    path('registrar/', registrar_producto, name="registrarProducto"),
    
]
