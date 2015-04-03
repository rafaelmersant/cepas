from django.db import models

from miembros.models import Miembro
from estatus.models import Estatus
from zonas.models import Zona

class Presbitero(models.Model):
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.ForeignKey(Estatus)


class Presbitero_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True)
	fecha_fin = models.DateField(blank=True)
	
	presbitero = models.ForeignKey(Presbitero)
	zona = models.ForeignKey(Zona)