# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.db import models

class Tipo(models.Model):
	descripcion = models.TextField(max_length=255)
	
	def __unicode__(self):
		return self.descripcion
