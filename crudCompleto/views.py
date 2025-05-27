from django.shortcuts import render
from crudCompleto.models import Productos
# Create your views here.

def listar_productos(request):
    productos = Productos.objects.all()  # Obtiene todos los productos de la BD
    return render(request, 'productos/listar.html', {'productos': productos})  # Pasar la variable
