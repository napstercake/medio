# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.db import models

from productos.models import Producto

class Galeria(models.Model):
	titulo = models.TextField(max_length=255, blank=True)
	descripcion = models.TextField(blank=True)
	imagen = models.ImageField(upload_to='gallery')
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return self.titulo

