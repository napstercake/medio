from django.db import models

# Create your models here.
from inmobiliarias.models import Inmobiliaria
from desarrollos.models import Desarrollo

class Proyecto(models.Model):
	titulo = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	web = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='img')
	inmobiliaria = models.ForeignKey(Inmobiliaria)
	desarrollo = models.ForeignKey(Desarrollo)
	
	def __unicode__(self):
		return self.titulo
