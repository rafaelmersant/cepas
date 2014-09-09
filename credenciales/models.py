from django.db import models

class Credencial(models.Model):
	descripcion = models.CharField(max_length=50)
	