from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Inventario
from .forms import ProductoForm, CategoriaForm, InventarioForm, BuscarProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = CategoriaForm()
    return render(request, 'productos/agregar_categoria.html', {'form': form})

def buscar_producto(request):
    form = BuscarProductoForm(request.GET)
    productos = Producto.objects.all()
    if form.is_valid():
        if form.cleaned_data['nombre']:
            productos = productos.filter(nombre__icontains=form.cleaned_data['nombre'])
        if form.cleaned_data['categoria']:
            productos = productos.filter(categoria=form.cleaned_data['categoria'])
    return render(request, 'productos/buscar_producto.html', {'form': form, 'productos': productos})
