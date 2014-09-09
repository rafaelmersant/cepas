from django.db import models

from iglesias.models import Iglesia
from miembros.models import Miembro
from estatus.models import Estatu

class Pastor(models.Model):
	tipo_pastor_choices = (('Titular','Titular'),('NTitular','No Titular'),)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.ForeignKey(Estatu)
	tipo_pastor = models.CharField(max_length=10,choices=tipo_pastor_choices)

	def __unicode__(self):
		return nombre


class Pastor_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True)
	fecha_fin = models.DateField(blank=True)

	pastor = models.ForeignKey(Pastor)
	iglesia = models.ForeignKey(Iglesia)
