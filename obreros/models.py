from django.db import models

from credenciales.models import Credencial
from estatus.models import Estatus
from iglesias.models import Iglesia
from pastores.models import Pastor
from miembros.models import Miembro

class Obrero(models.Model):

	anio_nombramiento = models.PositiveIntegerField()
	
	obrero = models.ForeignKey(Miembro)
	credencial = models.ForeignKey(Credencial)
	estatus = models.ForeignKey(Estatus)
	iglesia = models.ForeignKey(Iglesia)
	pastor = models.ForeignKey(Pastor)

	def __unicode__(self):
		return self.obrero