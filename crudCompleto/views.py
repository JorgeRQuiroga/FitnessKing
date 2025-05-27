from django.shortcuts import render
from crudCompleto.models import Productos
from crudCompleto.forms import ProductForm
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def listar_productos(request):
    productos = Productos.objects.all()  # Obtiene todos los productos de la BD
    return render(request, 'productos/listar.html', {'productos': productos})  # Pasar la variable

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