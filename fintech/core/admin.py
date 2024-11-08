from django.contrib import admin
from .models import ProductoFinanciero, Inversion  # Solo importa los modelos que están en core

# Registro de modelos en el panel de administración
admin.site.register(ProductoFinanciero)
admin.site.register(Inversion)
