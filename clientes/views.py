from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True).order_by('nombre')
    return render(request, 'clientes/lista.html', {'clientes': clientes})


@login_required
def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})


@login_required
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ruc = request.POST.get('ruc')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        Cliente.objects.create(
            nombre=nombre,
            ruc=ruc,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('lista_clientes')
    return render(request, 'clientes/formulario.html', {'titulo': 'Nuevo Cliente'})


@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.ruc = request.POST.get('ruc')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/formulario.html', {'titulo': 'Editar Cliente', 'cliente': cliente})


@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.activo = False
    cliente.save()
    return redirect('lista_clientes')