# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.db import models

from proyectos.models import Proyecto
from entregas.models import Entrega
from etapas.models import Etapa
from tipos.models import Tipo

class Producto(models.Model):
	titulo = models.TextField(max_length=255)
	descripcion = models.TextField()
	disponibles = models.IntegerField(null=True, blank=True)
	mt_cuadrados_const = models.FloatField()
	mt_terreno = models.FloatField()
	cant_departamentos = models.IntegerField(null=True, blank=True)
	cant_loc_comerciales = models.IntegerField(null=True, blank=True)
	cant_oficinas = models.IntegerField(null=True, blank=True)
	cant_edificios = models.IntegerField(null=True, blank=True)
	mail_contacto = models.CharField(max_length=255)
	proyecto = models.ForeignKey(Proyecto)
	entrega = models.ForeignKey(Entrega)
	etapa = models.ForeignKey(Etapa)
	tipo = models.ForeignKey(Tipo)
	
	def __unicode__(self):
		return self.titulo
