from django.db import models

from miembros.models import Miembro
from zonas.models import Zona

class Presbitero(models.Model):
	estatus_choices = (('A','Activo'),('I','Inactivo'))	

	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')


class Presbitero_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True)
	fecha_fin = models.DateField(blank=True)
	
	presbitero = models.ForeignKey(Presbitero)
	zona = models.ForeignKey(Zona)
