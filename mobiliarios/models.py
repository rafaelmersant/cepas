from django.db import models

from iglesias.models import Iglesia

class Mobiliario(models.Model):
	mobiliario = models.CharField(max_length=100, blank=True)
	cantidad = models.PositiveIntegerField()
	
	iglesia = models.ForeignKey(Iglesia)