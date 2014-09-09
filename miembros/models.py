# -*- coding: utf-8 -*-

from django.db import models

from cargos.models import Cargo
from iglesias.models import Iglesia
from estatus.models import Estatu
from areas.models import Area

class Miembro(models.Model):
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

	pareja_cristiana_choices = (
					 			 ('S','SI'),
					 			 ('N','NO'),
						   		)

	cedula_pasaporte 	= models.CharField(max_length=13)
	nombres 			= models.CharField(max_length=100)
	apellidos 			= models.CharField(max_length=100, blank=True)
	telefonos 			= models.CharField(max_length=100, blank=True)
	direccion 			= models.CharField(max_length=100, blank=True)
	correo 				= models.CharField(max_length=50, blank=True)
	sexo 				= models.CharField(max_length=1, choices=sexo_choices)
	estado_civil 		= models.CharField(max_length=1, choices=estado_civil_choices)
	dia_nacimiento 		= models.PositiveIntegerField(blank=True)
	mes_nacimiento 		= models.CharField(max_length=2, choices=mes_nacimiento_choices)
	anio_nacimiento 	= models.PositiveIntegerField(blank=True)
	sociedad 			= models.CharField(max_length=1, choices=sociedad_choices)
	bautizado 			= models.DateField(blank=True)
	fecha_bautismo 		= models.DateField(blank=True)
	fecha_profesionfe 	= models.DateField(blank=True)
	tipo_miembro 		= models.CharField(max_length=1, choices=tipo_miembro_choices)
	iglesia_procedencia = models.CharField(max_length=100, blank=True)
	habilidades 		= models.TextField(max_length=250, blank=True)
	fecha_boda 			= models.DateField(blank=True)
	nombre_de_pareja 	= models.CharField(max_length=100, blank=True)
	pareja_cristiana 	= models.CharField(max_length=1,choices=pareja_cristiana_choices)

	iglesia 			= models.ForeignKey(Iglesia)
	estatus 			= models.ForeignKey(Estatu)


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
	descripcion = models.TextField(max_length=300)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.ForeignKey(Estatu)