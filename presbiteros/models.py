from django.db import models

from miembros.models import Miembro
from estatus.models import Estatu
from zonas.models import Zona

class Presbitero(models.Model):
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.ForeignKey(Estatu)


class Presbitero_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True)
	fecha_fin = models.DateField(blank=True)
	
	presbitero = models.ForeignKey(Presbitero)
	zona = models.ForeignKey(Zona)