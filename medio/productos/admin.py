# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.contrib import admin

from .models import Producto
from galerias.models import Galeria

class GaleriaInline(admin.StackedInline):
	model = Galeria

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'mail_contacto', 'proyecto')
	inlines = [GaleriaInline, ]

admin.site.register(Producto, ProductoAdmin)
