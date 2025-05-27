from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('listar/', listar_productos, name='listarProductos'),
    path('registrar/', registrar_producto, name="registrarProducto"),
    path('editar/<int:id>/', editar_producto, name="editarProducto"),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminarProducto'),
    path('restaurar/', listar_productos_eliminados, name='restaurarProducto'),
    path('restaurar/<int:id>/', restaurar_producto, name='restaurarProductoLogico'),
]
