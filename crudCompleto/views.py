from django.shortcuts import render
from crudCompleto.models import *
from crudCompleto.forms import ProductForm
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
def inicio(request):
    return render(request, 'productos/index.html')  # Renderiza la plantilla de inicio
def listar_productos(request):
    productos = Productos.objects.filter(eliminado=False)  # Obtiene todos los productos de la BD
    return render(request, 'productos/listar.html', {'productos': productos})  # Pasar la variable
def listar_productos_eliminados(request):
	listar_productos_eliminados= Productos.objects.filter(eliminado=True)  # Obtiene los productos eliminados
	return render(request, 'productos/listar_eliminados.html', {'productos': listar_productos_eliminados})  # Pasar la variable
    
def registrar_producto(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listarProductos')
	else:
		form = ProductForm()
	return render(request, 'productos/form.html', {'form': form})
def editar_producto(request, id):
	producto = get_object_or_404(Productos, pk=id)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('listarProductos')
	else:
		form = ProductForm(instance=producto)
	return render(request, 'productos/editar.html', {'form': form})

def eliminar_producto(request, id):
	producto = get_object_or_404(Productos, pk=id)
	producto.delete()  # Borrado lógico
	return redirect('listarProductos')

def restaurar_producto(request, id):
	producto = get_object_or_404(Productos, pk=id)
	producto.restore()  # Restaurar producto
	return redirect('restaurarProducto')