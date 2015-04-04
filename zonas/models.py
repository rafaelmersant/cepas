# -*- coding: utf-8 -*-

from django.db import models

class Zona(models.Model):
	provincias_choices =(
						('1','Azua'),
						('2','Bahoruco'),
						('3','Barahona'),
						('4','Dajabon'),
						('5','Distrito Nacional'),
						('6','Duarte'),
						('7','Elias Piña'),
						('8','El Seibo'),
						('9','Espaillat'),
						('10','Hato Mayor'),
						('11','Hermanas Mirabal'),
						('12','Independencia'),
						('13','La Altagracia'),
						('14','La Romana'),
						('15','La Vega'),
						('16','Maria Trinidad Sanchez'),
						('17','Monseñor Nouel'),
						('18','Monte Cristi'),
						('19','Monte Plata'),
						('20','Pedernales'),
						('21','Peravia'),
						('22','Puerto Plata'),
						('23','Samaná'),
						('24','Sanchez Ramirez'),
						('25','San Cristobal'),
						('26','San Jose de Ocoa'),
						('27','San Juan'),
						('28','San Pedro de Macoris'),
						('29','Santiago'),
						('30','Santiago Rodriguez'),
						('31','Santo Domingo'),
						('32','Valverde'),
						('33','Internacional'),
						)
	Descripcion = models.CharField(max_length=80)
	Provincia = models.CharField(max_length=2, choices=provincias_choices)

	def __unicode__(self):
		return self.Descripcion