from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from proveedores.models import Proveedor
from inventario.models import Producto
from ventas.models import Venta
from compras.models import Compra


@login_required
def index(request):
    total_clientes = Cliente.objects.filter(activo=True).count()
    total_proveedores = Proveedor.objects.filter(activo=True).count()
    total_productos = Producto.objects.filter(activo=True).count()
    total_ventas = Venta.objects.filter(estado='completada').count()
    total_compras = Compra.objects.filter(estado='recibida').count()

    ultimas_ventas = Venta.objects.all().order_by('-fecha')[:5]
    ultimas_compras = Compra.objects.all().order_by('-fecha')[:5]

    context = {
        'total_clientes': total_clientes,
        'total_proveedores': total_proveedores,
        'total_productos': total_productos,
        'total_ventas': total_ventas,
        'total_compras': total_compras,
        'ultimas_ventas': ultimas_ventas,
        'ultimas_compras': ultimas_compras,
    }

    return render(request, 'dashboard/index.html', context)

@login_required
def hub(request):
    return render(request, 'hub.html')