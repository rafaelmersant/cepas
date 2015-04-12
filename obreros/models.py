# -*- coding: utf-8 -*-

# MODEL DE ADMINISTRACION

from django.db import models

from administracion.models import Iglesia, Pastor, Miembro


# Credenciales de Obreros: Obrero Inicial/Exhortador/Licenciado, Ministro Licenciado/Ordenado.
class Credencial(models.Model):
	descripcion = models.CharField(max_length=25, unique=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name = 'Credencial'
		verbose_name_plural = 'Credenciales'


# Miembros que son obreros
class Obrero(models.Model):
	estatus_choices = (('A','Activo'), ('I','Inactivo'))

	anio_nombramiento = models.PositiveIntegerField("Año nombramiento")
	
	obrero = models.ForeignKey(Miembro, unique=True)
	credencial = models.ForeignKey(Credencial)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	iglesia = models.ForeignKey(Iglesia)
	pastor = models.ForeignKey(Pastor)

	def __unicode__(self):
		return self.obrero.nombreCompleto

	class Meta:
		ordering = ('obrero','anio_nombramiento')


# Ascensos de obreros
class Ascenso(models.Model):
	
	anio = models.PositiveIntegerField("Año")

	obrero = models.ForeignKey(Obrero)	
	rango_nuevo = models.ForeignKey(Credencial)

	def __unicode__(self):
		return self.obrero.obrero.nombreCompleto

	class Meta:
		ordering = ('obrero','-anio')


# Cuotas de Obreros
class Cuota(models.Model):
	concepto = models.CharField(max_length=60)
	clave = models.CharField(max_length=3, blank=True, null=True)
	cuota = models.DecimalField(max_digits=8, decimal_places=2)

	def __unicode__(self):
		return self.concepto

	class Meta:
		ordering = ('concepto',)