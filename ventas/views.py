from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Venta, DetalleVenta
from clientes.models import Cliente
from inventario.models import Producto


@login_required
def lista_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')
    return render(request, 'ventas/lista.html', {'ventas': ventas})


@login_required
def detalle_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    detalles = venta.detalles.all()
    return render(request, 'ventas/detalle.html', {'venta': venta, 'detalles': detalles})


@login_required
def crear_venta(request):
    clientes = Cliente.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)
    if request.method == 'POST':
        numero = request.POST.get('numero')
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')
        venta = Venta.objects.create(
            numero=numero,
            cliente_id=cliente_id,
            estado=estado,
            observaciones=observaciones
        )
        productos_ids = request.POST.getlist('producto')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')
        total = 0
        for i in range(len(productos_ids)):
            if productos_ids[i]:
                detalle = DetalleVenta.objects.create(
                    venta=venta,
                    producto_id=productos_ids[i],
                    cantidad=cantidades[i],
                    precio_unitario=precios[i],
                    subtotal=0
                )
                total += detalle.subtotal
        venta.total = total
        venta.save()
        return redirect('lista_ventas')
    return render(request, 'ventas/formulario.html', {
        'titulo': 'Nueva Venta',
        'clientes': clientes,
        'productos': productos
    })


@login_required
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    venta.estado = 'anulada'
    venta.save()
    return redirect('lista_ventas')