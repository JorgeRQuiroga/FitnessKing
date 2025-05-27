from django.urls import path
from crudCompleto.views import *

urlpatterns = [
    path('', listar_productos, name='listarProductos'),
    path('editar/<int:id>/', editar_producto, name="editarProducto"),  # Agregar parámetro ID
    path('registrar/', registrar_producto, name="registrarProducto"),
    
]
