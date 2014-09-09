from django.db import models

class Area(models.Model):
	descripcion = models.CharField(max_length=100)
	