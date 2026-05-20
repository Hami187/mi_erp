from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Compra, DetalleCompra
from proveedores.models import Proveedor
from inventario.models import Producto


@login_required
def lista_compras(request):
    compras = Compra.objects.all().order_by('-fecha')
    return render(request, 'compras/lista.html', {'compras': compras})


@login_required
def detalle_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    detalles = compra.detalles.all()
    return render(request, 'compras/detalle.html', {'compra': compra, 'detalles': detalles})


@login_required
def crear_compra(request):
    proveedores = Proveedor.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)
    if request.method == 'POST':
        numero = request.POST.get('numero')
        proveedor_id = request.POST.get('proveedor')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')
        compra = Compra.objects.create(
            numero=numero,
            proveedor_id=proveedor_id,
            estado=estado,
            observaciones=observaciones
        )
        productos_ids = request.POST.getlist('producto')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')
        total = 0
        for i in range(len(productos_ids)):
            if productos_ids[i]:
                detalle = DetalleCompra.objects.create(
                    compra=compra,
                    producto_id=productos_ids[i],
                    cantidad=cantidades[i],
                    precio_unitario=precios[i],
                    subtotal=0
                )
                total += detalle.subtotal
        compra.total = total
        compra.save()
        return redirect('lista_compras')
    return render(request, 'compras/formulario.html', {
        'titulo': 'Nueva Compra',
        'proveedores': proveedores,
        'productos': productos
    })


@login_required
def eliminar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    compra.estado = 'anulada'
    compra.save()
    return redirect('lista_compras')