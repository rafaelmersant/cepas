from django.db import models

from credenciales.models import Credencial
from iglesias.models import Iglesia
from pastores.models import Pastor
from miembros.models import Miembro

class Obrero(models.Model):
	estatus_choices = (('A','Activo'), ('I','Inactivo'))

	anio_nombramiento = models.PositiveIntegerField()
	
	obrero = models.ForeignKey(Miembro)
	credencial = models.ForeignKey(Credencial)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	iglesia = models.ForeignKey(Iglesia)
	pastor = models.ForeignKey(Pastor)

	def __unicode__(self):
		return self.obrero
