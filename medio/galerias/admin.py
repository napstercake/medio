# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.contrib import admin

from .models import Galeria
from sorl.thumbnail import get_thumbnail

class GaleriaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'descripcion', 'imagen_galeria')

	def imagen_galeria(self, obj):
		return '<img src="%s"' % get_thumbnail(obj.imagen, '390x90').url

	imagen_galeria.allow_tags = True

admin.site.register(Galeria, GaleriaAdmin)
