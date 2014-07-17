# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.db import models

class Inmobiliaria(models.Model):
	razon_social = models.CharField(max_length=255)
	nombre_comercial = models.CharField(max_length=255, blank=True)
	ruc = models.BigIntegerField()
	direccion = models.CharField(max_length=255)
	telefono_fijo_1 = models.CharField(max_length=30)
	telefono_fijo_2 = models.CharField(max_length=30, blank=True)
	telefono_celular_1 = models.CharField(max_length=50, blank=True)
	telefono_celular_2 = models.CharField(max_length=50, blank=True)
	telefono_celular_3 = models.CharField(max_length=50, blank=True)
	web = models.CharField(max_length=255, blank=True)
	logo = models.ImageField(upload_to='img')

	def __unicode__(self):
		return self.razon_social
    