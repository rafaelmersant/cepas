# -*- coding: utf-8 -*-

# MODEL DE REUNIONES

from django.db import models

from obreros.models import Obrero

# Tipos de Reuniones
class Tipo_Reunion(models.Model):
	descripcion = models.CharField(max_length=100, unique=True)
	observacion = models.TextField(max_length=350, null=True, blank=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('descripcion',)
		verbose_name = 'Tipo de Reunion'
		verbose_name_plural = 'Tipos de Reuniones'


# Reuniones
class Reunion(models.Model):
	reunion_choices = (
						('O','Ordinaria'),
						('E','Extraordinaria'),
					  )
	clase_reunion = models.CharField(max_length=1, choices=reunion_choices, default='O')
	fecha = models.DateField(unique=True)
	lugar = models.CharField(max_length=150, blank=True, null=True)
	
	tipo_reunion = models.ForeignKey(Tipo_Reunion)

	def __unicode__(self):
		return self.fecha

	class Meta:
		ordering = ('fecha',)
		verbose_name = 'Reunion'
		verbose_name_plural = 'Reuniones'


# Asistencia a las reuniones
class Asistencia(models.Model):
	motivo_choices = (
						('P','Presente'),
						('A','Ausente'),
						('E','Excusa'),
					 )

	motivo = models.CharField(max_length=1, choices=motivo_choices, default='P')
	pago = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	excusa_descrp = models.TextField(max_length=200, blank=True, null=True)

	obrero = models.ForeignKey(Obrero)
	reunion = models.ForeignKey(Reunion)

	def __unicode__(self):
		return self.obrero

	class Meta:
		ordering = ('obrero',)
