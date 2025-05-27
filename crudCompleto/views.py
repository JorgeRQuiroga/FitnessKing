
from crudCompleto.models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
# Create your views here.

def listar_productos(request):
	productos = Producto.objects.all()
	return render(request, 'productos\listar.html', {'productos': Producto})

def registrar_producto(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listarProductos')
	else:
		form = ProductForm()
	return render(request, 'productos/form.html', {'form': form})


def editar_producto(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('listarproductos')
	else:
		form = ProductForm(instance=producto)
	return render(request, 'productos/editar.html', {'form': form})