from django.shortcuts import render

# Create your views here.
def agregar_producto(request):
    if request.method == 'POST':
        pass

    return render(request, 'agregar_producto.html')
