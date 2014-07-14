# Estudio Collective.
#
# Propiedad de Estudio Collective
# @author Ricardo Gonzales (rgonzales@collective.pe)
# 
# Todos los derechos reservados.

from django.db import models

from productos.models import Producto

class Construccion(models.Model):
	descripcion = models.TextField(max_length=255)
	cant_dormitorios = models.IntegerField(null=True, blank=True)
	nro_estacionamientos = models.IntegerField(null=True, blank=True)
	nro_pisos = models.IntegerField(null=True, blank=True)
	nro_banos_completos = models.IntegerField(null=True, blank=True)
	nro_banos_medios = models.IntegerField(null=True, blank=True)
	precio = models.FloatField()
	observaciones = models.TextField(blank=True)
	tipo_dpto = models.TextField(max_length=255)
	terraza = models.BooleanField()
	balcon = models.BooleanField()
	cuarto_servicio = models.BooleanField()
	piscina = models.BooleanField()
	jardin = models.BooleanField()
	ascensor = models.BooleanField()
	frente_al_parque = models.BooleanField()
	cerca_hospital = models.BooleanField()
	frente_al_mar = models.BooleanField()
	lavanderia = models.BooleanField()
	areas_verdes = models.BooleanField()
	canchas_deportivas = models.BooleanField()
	gimnasio = models.BooleanField()
	juegos_infantiles = models.BooleanField()
	parrilla = models.BooleanField()
	sala_computo = models.BooleanField()
	sala_reuniones = models.BooleanField()
	estado = models.BooleanField()
	tipo = models.BooleanField()
	usado = models.BooleanField()
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return self.descripcion