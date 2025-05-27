from django.shortcuts import render
from crudCompleto.models import *
# Create your views here.

def listar_productos(request):
	productos = Producto.objects.all()
	return render(request, 'productos\listar.html', {'productos': Producto})