from django.db import models

class Tipo_Reunion(models.Model):
	descripcion = models.CharField(max_length=100)
	observacion = models.TextField(max_length=350)


class Reunion(models.Model):
	reunion_choices = (
						('O','Ordinaria'),
						('E','Extraordinaria'),
					  )
	clase_reunion = models.CharField(max_length=1, choices=reunion_choices)
	fecha = models.DateField()
	lugar = models.CharField(max_length=150, blank=True)
	
	tipo_reunion = models.ForeignKey(Tipo_Reunion)