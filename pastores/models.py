from django.db import models

from iglesias.models import Iglesia
from miembros.models import Miembro

class Pastor(models.Model):
	estatus_choices = (('A','Activo'),('I','Inactivo'))
	tipo_pastor_choices = (('Titular','Titular'),('NTitular','No Titular'),)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	tipo_pastor = models.CharField(max_length=10,choices=tipo_pastor_choices)

	def __unicode__(self):
		return nombre

	class Meta:
		verbose_name = 'Pastor'
		verbose_name_plural = 'Pastores'


class Pastor_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True)
	fecha_fin = models.DateField(blank=True)

	pastor = models.ForeignKey(Pastor)
	iglesia = models.ForeignKey(Iglesia)
