from django.db import models

from iglesias.models import Iglesia
from miembros.models import Miembro

class Caso(models.Model):
	estatus_casos_choices = (
							 ('A','Abierto'),
							 ('C','Cerrado'),
							)
	descripcion = models.TextField(max_length=500, blank=True)
	estatus = models.CharField(max_length=1,choices=estatus_casos_choices)

	iglesia = models.ForeignKey(Iglesia)
	miembro = models.ForeignKey(Miembro)
