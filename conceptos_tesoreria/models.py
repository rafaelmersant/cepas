from django.db import models

class Concepto_Tesoreria(models.Model):
	tipo_choices = (
					 ('D','Debito'),
					 ('C','Credito'),
					)
	descripcion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1,choices=tipo_choices)