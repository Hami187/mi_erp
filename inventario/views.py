from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria


@login_required
def lista_productos(request):
    productos = Producto.objects.filter(activo=True).order_by('nombre')
    return render(request, 'inventario/lista.html', {'productos': productos})


@login_required
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/detalle.html', {'producto': producto})


@login_required
def crear_producto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        precio_compra = request.POST.get('precio_compra')
        precio_venta = request.POST.get('precio_venta')
        stock = request.POST.get('stock')
        stock_minimo = request.POST.get('stock_minimo')
        Producto.objects.create(
            codigo=codigo,
            nombre=nombre,
            descripcion=descripcion,
            categoria_id=categoria_id,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            stock=stock,
            stock_minimo=stock_minimo
        )
        return redirect('lista_productos')
    return render(request, 'inventario/formulario.html', {'titulo': 'Nuevo Producto', 'categorias': categorias})


@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.categoria_id = request.POST.get('categoria')
        producto.precio_compra = request.POST.get('precio_compra')
        producto.precio_venta = request.POST.get('precio_venta')
        producto.stock = request.POST.get('stock')
        producto.stock_minimo = request.POST.get('stock_minimo')
        producto.save()
        return redirect('lista_productos')
    return render(request, 'inventario/formulario.html', {'titulo': 'Editar Producto', 'producto': producto, 'categorias': categorias})


@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.activo = False
    producto.save()
    return redirect('lista_productos')