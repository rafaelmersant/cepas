from django.db import models

from estatus.models import Estatu
from miembros.models import Miembro
from iglesias.models import Iglesia

class CampoBlanco(models.Model):

	direccion = models.TextField(max_length=200, blank=True)
	telefono_contacto = models.CharField(max_length=50, blank=True)
	fecha_inicio = models.DateField(blank=True)
	observacion = models.CharField(max_length=100, blank=True)
	
	estatus = models.ForeignKey(Estatu)
	encargado = models.ForeignKey(Miembro)
	iglesia = models.ForeignKey(Iglesia)
