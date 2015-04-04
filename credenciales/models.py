from django.db import models

class Credencial(models.Model):
	descripcion = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Credencial'
		verbose_name_plural = 'Credenciales'

	
