# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.contrib import admin

from actions import export_as_excel

from .models import Proyecto
from sorl.thumbnail import get_thumbnail

class ProyectoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'inmobiliaria', 'logo_proyecto', 'web', 'desarrollo')
	list_filter = ('inmobiliaria', 'desarrollo')
	search_fields = ('titulo', 'inmobiliaria__razon_social')	
	actions = (export_as_excel, )

	def logo_proyecto(self, obj):
		return '<img src="%s"' % get_thumbnail(obj.logo, '50x50').url

	logo_proyecto.allow_tags = True

admin.site.register(Proyecto, ProyectoAdmin)