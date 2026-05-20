from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Proveedor


@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.filter(activo=True).order_by('nombre')
    return render(request, 'proveedores/lista.html', {'proveedores': proveedores})


@login_required
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle.html', {'proveedor': proveedor})


@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ruc = request.POST.get('ruc')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        contacto = request.POST.get('contacto')
        Proveedor.objects.create(
            nombre=nombre,
            ruc=ruc,
            email=email,
            telefono=telefono,
            direccion=direccion,
            contacto=contacto
        )
        return redirect('lista_proveedores')
    return render(request, 'proveedores/formulario.html', {'titulo': 'Nuevo Proveedor'})


@login_required
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.ruc = request.POST.get('ruc')
        proveedor.email = request.POST.get('email')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.save()
        return redirect('lista_proveedores')
    return render(request, 'proveedores/formulario.html', {'titulo': 'Editar Proveedor', 'proveedor': proveedor})


@login_required
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.activo = False
    proveedor.save()
    return redirect('lista_proveedores')