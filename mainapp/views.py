from django.shortcuts import render
from productos.models import Producto, CategoriaProducto

# Create your views here.
def index(request):

  categorias = CategoriaProducto.objects.all()
  productos = Producto.objects.filter(publico=True)
  cattmp = Producto.objects.filter(categoria=1)
  
  return render(request, 'mainapp/index.html', {
    'titulo':'Home',
    'categorias':categorias,
    'productos':productos,
    'cattmp':cattmp
  })