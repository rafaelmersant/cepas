from django.db import models

class Cuota(models.Model):
	concepto = models.CharField(max_length=60)
	clave = models.CharField(max_length=3, blank=True)
	cuota = models.DecimalField(max_digits=8, decimal_places=2)