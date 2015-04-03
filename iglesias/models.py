from django.db import models

from zonas.models import Zona
from estatus.models import Estatus

class Iglesia(models.Model):
	tipo_iglesia_choices = (
							('M','Miembro'),
							('A','Asociada'),
						   )
	tipo_local_choices = (
							('P','Propio'),
							('A','Alquilado'),
							('D','Desconocido'),
				 		 )

	titulo_conciliar 	= models.CharField(max_length=150)
	titulo_local 		= models.CharField(max_length=150, blank=True)
	direccion 			= models.TextField(max_length=200, blank=True)
	telefono_contacto 	= models.CharField(max_length=50, blank=True)
	tipo_iglesia 		= models.CharField(max_length=1,choices=tipo_iglesia_choices)
	denominacion_origen = models.CharField(max_length=100, blank=True)
	fecha_fundacion		= models.DateField(blank=True)
	local				= models.CharField(max_length=1, choices=tipo_local_choices)
	observacion			= models.TextField(max_length=100, blank=True)

	estatus				= models.ForeignKey(Estatus)
	zona 				= models.ForeignKey(Zona)

	
	def  __unicode__(self):
		return self.titulo_conciliar
