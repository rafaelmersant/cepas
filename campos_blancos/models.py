from django.db import models

from miembros.models import Miembro
from iglesias.models import Iglesia

class CampoBlanco(models.Model):
	estatus_choices = (('A','Activo'), ('I','Inactivo'))

	direccion = models.TextField(max_length=200, blank=True)
	telefono_contacto = models.CharField(max_length=50, blank=True)
	fecha_inicio = models.DateField(blank=True)
	observacion = models.CharField(max_length=100, blank=True)
	
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	encargado = models.ForeignKey(Miembro)
	iglesia = models.ForeignKey(Iglesia)
