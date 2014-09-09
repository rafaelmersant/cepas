from django.db import models

from credenciales.models import Credencial
from obreros.models import Obrero

class Ascenso(models.Model):
	
	anio = models.PositiveIntegerField()

	obrero = models.ForeignKey(Obrero)	
	
	# rango_anterior = models.ForeignKey(Credencial)
	rango_nuevo = models.ForeignKey(Credencial)