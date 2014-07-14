# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.contrib import admin

# Register your models here.
from .models import Inmobiliaria
from sorl.thumbnail import get_thumbnail

class InmobiliariaAdmin(admin.ModelAdmin):
	list_display = ('razon_social', 'ruc', 'direccion', 'telefono_fijo_1', 'telefono_celular_1', 'web', 'logo_inmobiliaria')
	search_fields = ('razon_social', 'ruc')
	
	def logo_inmobiliaria(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.logo, '50x50').url
		
	logo_inmobiliaria.allow_tags = True	
	
	

admin.site.register(Inmobiliaria, InmobiliariaAdmin)
