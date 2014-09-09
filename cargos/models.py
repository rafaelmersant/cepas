from django.db import models

from areas.models import Area

class Tipo_Cargo(models.Model):
	descripcion = models.CharField(max_length=100)


class Cargo(models.Model):
	
	descripcion = models.CharField(max_length=100)
	nivel = models.PositiveIntegerField()
	
	tipo_cargo = models.ForeignKey(Tipo_Cargo)
	area = models.ForeignKey(Area)
