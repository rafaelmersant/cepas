from django.db import models

from obreros.models import Obrero

class Asistencia(models.Model):
	motivo_choices = (
						('P','Presente'),
						('A','Ausente'),
						('E','Excusa'),
					 )

	motivo = models.CharField(max_length=1, choices=motivo_choices)
	pago = models.DecimalField(max_digits=8, decimal_places=2)
	excusa_descrp = models.TextField(max_length=200, blank=True)

	obrero = models.ForeignKey(Obrero)