# -*- coding: utf-8 -*-

from django.db import models

from cargos.models import Cargo
from iglesias.models import Iglesia
from areas.models import Area

class Miembro(models.Model):
	estatus_choices = (
					 ('A','Activo'),
					 ('I','Inactivo'),
					)

	sexo_choices = (
					 ('F','Femenino'),
					 ('M','Masculino'),
					)

	estado_civil_choices = (
					 		('S','Soltero(a)'),
					 		('C','Casado(a)'),
						   )

	mes_nacimiento_choices = (
								('01','Enero'),
								('02','Febrero'),
								('03','Marzo'),
								('04','Abril'),
								('05','Mayo'),
								('06','Junio'),
								('07','Julio'),
								('08','Agosto'),
								('09','Septiembre'),
								('10','Octubre'),
								('11','Noviembre'),
								('12','Diciembre'),
							 )

	sociedad_choices = (
						 ('D','Damas'),
						 ('C','Caballeros'),
						 ('J','Jovenes'),
						 ('A','Adolescentes'),
						 ('N','Niños'),
					   )

	tipo_miembro_choices = (
					 		('M','Miembro'),
					 		('A','Asociado'),
						   )
	
	bautizado_choices = (
					 	 ('N','NO'),
					 	 ('S','SI'),
						)
	
	pareja_cristiana_choices = (
					 			 ('S','SI'),
					 			 ('N','NO'),
						   		)

	cedula_pasaporte 	= models.CharField("Cedula o Pasaporte", max_length=13, blank=True, null=True)
	nombres 			= models.CharField(max_length=40)
	apellidos 			= models.CharField(max_length=40, blank=True, null=True)
	telefonos 			= models.CharField(max_length=50, blank=True, null=True)
	direccion 			= models.CharField(max_length=150, blank=True, null=True)
	correo 				= models.CharField(max_length=50, blank=True, null=True)
	sexo 				= models.CharField(max_length=1, choices=sexo_choices)
	estado_civil 		= models.CharField(max_length=1, choices=estado_civil_choices, null=True)
	dia_nacimiento 		= models.PositiveIntegerField(blank=True, null=True)
	mes_nacimiento 		= models.CharField(max_length=2, choices=mes_nacimiento_choices, blank=True, null=True)
	anio_nacimiento 	= models.PositiveIntegerField("Año nacimiento", blank=True, null=True)
	sociedad 			= models.CharField(max_length=1, choices=sociedad_choices, blank=True, null=True)
	bautizado 			= models.CharField(max_length=2, choices=bautizado_choices, default='N', blank=True, null=True)
	fecha_bautismo 		= models.DateField(blank=True, null=True)
	fecha_profesionfe 	= models.DateField(blank=True, null=True)
	tipo_miembro 		= models.CharField(max_length=1, choices=tipo_miembro_choices, default='M', null=True)
	iglesia_procedencia = models.CharField(max_length=100, blank=True, null=True)
	habilidades 		= models.TextField(max_length=250, blank=True, null=True)
	fecha_boda 			= models.DateField(blank=True, null=True)
	nombre_de_pareja 	= models.CharField(max_length=100, blank=True, null=True)
	pareja_cristiana 	= models.CharField(max_length=1,choices=pareja_cristiana_choices, blank=True, null=True)

	iglesia 			= models.ForeignKey(Iglesia, blank=True, null=True)
	estatus 			= models.CharField(max_length=1, choices=estatus_choices, default='A')

	def __unicode__(self):
		return '%s %s' % (self.nombres, self.apellidos)

	class Meta:
		ordering = ('nombres',)


class Miembro_Cargo(models.Model):
	anio_inicio = models.PositiveIntegerField()
	anio_fin = models.PositiveIntegerField()

	miembro = models.ForeignKey(Miembro)
	cargo = models.ForeignKey(Cargo)


class Curso_Miembro(models.Model):
	nivel_choices = (
					 ('L','Taller'),
					 ('T','Tecnico'),
					 ('U','Unversitario'),
					 ('O','Otro'),
					)

	curso_descripcion = models.CharField(max_length=150, blank=True)
	institucion = models.CharField(max_length=150, blank=True)
	anio = models.PositiveIntegerField()
	nivel = models.CharField(max_length=1, choices=nivel_choices)

	miembro = models.ForeignKey(Miembro)

class TrabajoRealizado(models.Model):
	descripcion = models.TextField(max_length=300)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	area = models.ForeignKey(Area)

class TrayectoriaMiembro(models.Model):
	estatus_choices = (
				 ('A','Activo'),
				 ('I','Inactivo'),
				)

	descripcion = models.TextField(max_length=300)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')