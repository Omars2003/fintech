# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/invertir/', views.invertir, name='invertir'),
    # No incluye rutas de login o logout
]
