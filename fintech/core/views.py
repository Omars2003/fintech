# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductoFinanciero, Inversion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def lista_productos(request):
    productos = ProductoFinanciero.objects.all()
    return render(request, 'core/productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(ProductoFinanciero, id=producto_id)
    return render(request, 'core/detalle_producto.html', {'producto': producto})

@login_required
def invertir(request, producto_id):
    producto = get_object_or_404(ProductoFinanciero, id=producto_id)
    if request.method == 'POST':
        monto = request.POST.get('monto')
        try:
            monto = float(monto)
            if monto <= 0:
                messages.error(request, "Por favor, ingresa un monto positivo.")
                return redirect('core:invertir', producto_id=producto_id)
        except ValueError:
            messages.error(request, "Monto inválido. Por favor, ingresa un número.")
            return redirect('core:invertir', producto_id=producto_id)
        Inversion.objects.create(usuario=request.user, producto_financiero=producto, monto=monto)
        messages.success(request, "¡Inversión realizada con éxito!")
        return redirect('core:lista_productos')
    return render(request, 'core/invertir.html', {'producto': producto})
