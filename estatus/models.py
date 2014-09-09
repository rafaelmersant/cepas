from django.db import models

class Estatu(models.Model):
	para_choices = (
					('M','Miembro'),
					('O','Obrero'),
					('P','Pastor'),
					('E','Presbitero'),
					('I','Iglesia'),
					('C','Campo Blanco')
					)
	descripcion = models.CharField(max_length=50)
	para = models.CharField(max_length=1, choices=para_choices)

	def __unicode__(self):
		return self.descripcion