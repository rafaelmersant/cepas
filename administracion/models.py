# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


#MMMMMMMMMMMMMMMMMMMMMMMMMMM
# ADMINISTRACION GENERAL
#MMMMMMMMMMMMMMMMMMMMMMMMMMM

# Areas
class Area(models.Model):
	descripcion = models.CharField(max_length=70)

	def __unicode__(self):
		return self.descripcion

	def save(self, *args, **kwargs):
		self.descripcion = self.descripcion.upper()

		super(Area, self).save(*args, **kwargs)

	class Meta:
		ordering = ('descripcion',)
		verbose_name = 'Area'
		verbose_name_plural = '4) Areas'


# Tipos de Cargos
class Tipo_Cargo(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('descripcion',)
		verbose_name = "Tipo de Cargo"
		verbose_name_plural = "5) Tipos de Cargos"


# Cargos
class Cargo(models.Model):
	
	descripcion = models.CharField(max_length=100, unique=True)
	# nivel = models.PositiveIntegerField()
	
	tipo_cargo = models.ForeignKey(Tipo_Cargo)
	area = models.ForeignKey(Area)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('descripcion',)
		verbose_name = 'Cargo'
		verbose_name_plural = '6) Cargos'


# Zonas (Presbiterales - Iglesias)
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
	descripcion = models.CharField(max_length=80)
	provincia = models.CharField(max_length=2, choices=provincias_choices)

	def __unicode__(self):
		return self.descripcion

	def save(self, *args, **kwargs):
		self.descripcion = self.descripcion.upper()

		super(Zona, self).save(*args, **kwargs)

	@property
	def Presbitero(self):
		try:
			p = Presbitero_Asign.objects.get(fecha_fin='9999-12-31', zona__id=self.id)
			presbitero = p.presbitero.miembro.nombreCompleto
		except Exception as e:
			presbitero = 'NO ASIGNADO'
		return presbitero

	class Meta:
		ordering = ('descripcion',)
		verbose_name_plural = '7) Zonas'


# Conceptos de Tesoreria  -- USO FUTURO
class Concepto_Tesoreria(models.Model):
	tipo_choices = (
					 ('D','Debito'),
					 ('C','Credito'),
					)
	descripcion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1,choices=tipo_choices)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('descripcion',)


# Iglesias
class Iglesia(models.Model):
	estatus_choices = (('A','Activo'),('I','Inactivo'))

	tipo_iglesia_choices = (
							('M','Miembro'),
							('A','Asociada'),
						   )
	tipo_local_choices = (
							('P','Propio'),
							('A','Alquilado'),
							('D','Desconocido'),
				 		 )

	titulo_conciliar 	= models.CharField(max_length=150)
	titulo_local 		= models.CharField(max_length=150, blank=True)
	direccion 			= models.TextField(max_length=200, blank=True)
	telefono_contacto 	= models.CharField(max_length=50, blank=True)
	tipo_iglesia 		= models.CharField(max_length=1,choices=tipo_iglesia_choices, default='M', blank=True)
	denominacion_origen = models.CharField(max_length=100, blank=True)
	fecha_fundacion		= models.DateField(blank=True, null=True)
	local				= models.CharField(max_length=1, choices=tipo_local_choices, blank=True)
	observacion			= models.TextField(max_length=100, blank=True)

	estatus				= models.CharField(max_length=1, choices=estatus_choices, default='A')
	zona 				= models.ForeignKey(Zona, null=True, blank=True)

	creadaFecha			= models.DateTimeField(auto_now_add=True)
	creadaPor			= models.ForeignKey(User, null=True, editable=False)
	modificada			= models.DateTimeField(auto_now=True)
	modificadaPor		= models.ForeignKey(User, null=True, editable=False, related_name='+')

	def  __unicode__(self):
		return self.titulo_conciliar
	
	def save(self, *args, **kwargs):
		self.titulo_conciliar = self.titulo_conciliar.upper()
		self.titulo_local = self.titulo_local.upper()

		super(Iglesia, self).save(*args, **kwargs)

	@property 
	def Pastor(self):
		try:
			p = Pastor_Asign.objects.get(fecha_fin='9999-12-31', iglesia__id=self.id)
			pastor = p.pastor.miembro.nombreCompleto
		except Exception as e:
			pastor = 'NO ASIGNADO'
		return pastor

	class Meta:
		ordering = ('titulo_conciliar',)
		verbose_name = 'Iglesia'
		verbose_name_plural = '1) Iglesias'


# Miembros en general
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
	habilidades 		= models.TextField("Habilidades (separadas por coma)", max_length=250, blank=True, null=True)
	fecha_boda 			= models.DateField(blank=True, null=True)
	nombre_de_pareja 	= models.CharField(max_length=100, blank=True, null=True)
	pareja_cristiana 	= models.CharField(max_length=1,choices=pareja_cristiana_choices, blank=True, null=True)
	foto				= models.FileField(upload_to='cepas/static/media/fotos/', null=True, blank=True)

	iglesia 			= models.ForeignKey(Iglesia, blank=True, null=True)
	estatus 			= models.CharField(max_length=1, choices=estatus_choices, default='A')

	creadaFecha			= models.DateTimeField(auto_now_add=True)
	creadaPor			= models.ForeignKey(User, null=True, editable=False)
	modificada			= models.DateTimeField(auto_now=True)
	modificadaPor		= models.ForeignKey(User, null=True, editable=False, related_name='+')

	def __unicode__(self):
		return '%s %s' % (self.nombres, self.apellidos)
	
	def save(self, *args, **kwargs):
		self.nombres = self.nombres.upper()
		self.apellidos = self.apellidos.upper()
		self.nombre_de_pareja = self.nombre_de_pareja.upper() if self.nombre_de_pareja != None else ''

		super(Miembro, self).save(*args, **kwargs)

	@property
	def nombreCompleto(self):
		return '%s %s' % (self.nombres, self.apellidos)

	class Meta:
		ordering = ('nombres',)
		verbose_name = 'Miembro'
		verbose_name_plural = '3) Miembros'


# Padres de Miembro (Esto es obligatorio para niños y adolescentes)
class Miembro_Padres(models.Model):
	choices_cristiano = (('S','SI'), ('N','NO'))

	miembro = models.ForeignKey(Miembro)
	madre = models.CharField("Madre (o tutora)", max_length=80, null=True, blank=True)
	madreCristiana = models.CharField("Madre (o tutora) Cristiana?", max_length=1, choices=choices_cristiano, default='S')
	padre = models.CharField("Padre (o tutor)", max_length=80, null=True, blank=True)
	padreCristiano = models.CharField("Padre (o tutor) Cristiano?", max_length=1, choices=choices_cristiano, default='S')

	def __unicode__(self):
		return 'Madre: %s - Padre: %s' % (self.madre, self.padre)
	
	def save(self, *args, **kwargs):
		self.madre = self.madre.upper()
		self.padre = self.padre.upper()

		super(Miembro_Padres, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Padres de Miembros (Obligatorio para niños y/o adolescentes"
		verbose_name_plural = "Padres de Miembros (Obligatorio para niños y/o adolescentes"


# Hijos Miembros
class Miembro_Hijos(models.Model):
	miembro = models.ForeignKey(Miembro)
	nombreHijo = models.CharField("Nombre de Hijo(a)", max_length=80, null=True, blank=True)
	fechaNacimiento = models.DateField("Fecha de Nacimiento", null=True, blank=True)

	def __unicode__(self):
		return self.nombreHijo
		
	def save(self, *args, **kwargs):
		self.nombreHijo = self.nombreHijo.upper()

		super(Miembro_Hijos, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Hijo de Miembro'
		verbose_name_plural = 'Hijos de Miembro'


# Cargos relacionados al miembro
class Miembro_Cargo(models.Model):
	anio_inicio = models.PositiveIntegerField("Año Inicio", null=True, blank=True)
	anio_fin = models.PositiveIntegerField("Año Fin", default=9999, null=True, blank=True)

	miembro = models.ForeignKey(Miembro)
	cargo = models.ForeignKey(Cargo)

	def __unicode__(self):
		return '%s %s' % (self.miembro.nombres, self.miembro.apellidos)

	class Meta:
		ordering = ('miembro',)
		verbose_name = 'Cargo de Miembro'
		verbose_name_plural = 'Cargos de Miembro'


# Cursos realizados por el miembro (tanto seculares como eclesiasticos)
class Curso_Miembro(models.Model):
	nivel_choices = (
					 ('L','Taller'),
					 ('T','Tecnico'),
					 ('U','Unversitario'),
					 ('O','Otro'),
					)

	clasificacion_choices = (('E','Eclesiastico'), ('S','Secular'))

	curso_descripcion = models.CharField(max_length=150, blank=True)
	institucion = models.CharField(max_length=150, blank=True)
	anio_inicio = models.PositiveIntegerField("Año Inicio", null=True, blank=True)
	anio_fin = models.PositiveIntegerField("Año Fin", null=True, blank=True)
	nivel = models.CharField(max_length=1, choices=nivel_choices)
	clasificacion = models.CharField(max_length=1, choices=clasificacion_choices, blank=True, null=True)

	miembro = models.ForeignKey(Miembro)

	def __unicode__(self):
		return self.curso_descripcion

	class Meta:
		ordering = ('miembro', 'curso_descripcion')
		verbose_name = 'Curso de Miembro'
		verbose_name_plural = 'Cursos de Miembros'


# Trabajos Realizados por el miembro
class TrabajoRealizado(models.Model):
	descripcion = models.TextField(max_length=300)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	area = models.ForeignKey(Area)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('miembro', 'descripcion')
		verbose_name = 'Trabajo Realizado'
		verbose_name_plural = 'Trabajos Realizados'


# Trayectoria del miembro
class TrayectoriaMiembro(models.Model):
	estatus_choices = (
				 ('A','Activo'),
				 ('I','Inactivo'),
				)

	descripcion = models.TextField(max_length=300)
	fecha = models.DateField()

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('miembro','fecha')
		verbose_name = 'Trayectoria Miembro'
		verbose_name_plural = 'Trayectorias de Miembros'


# Algun caso especifico con el miembro -- USO FUTURO
class Caso(models.Model):
	estatus_casos_choices = (
							 ('A','Abierto'),
							 ('C','Cerrado'),
							)
	descripcion = models.TextField(max_length=500, blank=True)
	estatus = models.CharField(max_length=1,choices=estatus_casos_choices)

	iglesia = models.ForeignKey(Iglesia)
	miembro = models.ForeignKey(Miembro)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		ordering = ('miembro','descripcion')


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# PASTORES
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

# Pastores
class Pastor(models.Model):
	estatus_choices = (('A','Activo'),('I','Inactivo'))
	tipo_pastor_choices = (('Titular','Titular'),('NTitular','No Titular'),)

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	tipo_pastor = models.CharField(max_length=10,choices=tipo_pastor_choices)

	def __unicode__(self):
		return '%s %s' % (self.miembro.nombres, self.miembro.apellidos)

	class Meta:
		verbose_name = 'Pastor'
		verbose_name_plural = 'Pastores'


# Cuando un pastor es asignado en un iglesia
class Pastor_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True, null=True)
	fecha_fin = models.DateField(blank=True, null=True, default='31/12/9999')

	pastor = models.ForeignKey(Pastor)
	iglesia = models.ForeignKey(Iglesia)

	def __unicode__(self):
		return '%s' % (self.fecha_inicio)

	class Meta:
		verbose_name = 'Pastor asignado'
		verbose_name_plural = 'Pastores Asignados'


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# PRESBITEROS
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

# Presbiteros
class Presbitero(models.Model):
	estatus_choices = (('A','Activo'),('I','Inactivo'))	

	fecha = models.DateField(auto_now_add=True)

	miembro = models.ForeignKey(Miembro)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')

	def __unicode__(self):
		return '%s %s' % (self.miembro.nombres, self.miembro.apellidos)

	class Meta:
		ordering = ('miembro',)


# Cuando el presbitero es asignado a una zona
class Presbitero_Asign(models.Model):
	fecha_inicio = models.DateField(blank=True, null=True)
	fecha_fin = models.DateField(blank=True, null=True, default='31/12/9999')
	
	presbitero = models.ForeignKey(Presbitero)
	zona = models.ForeignKey(Zona)

	def __unicode__(self):
		return '%s' % (self.fecha_inicio)

	class Meta:
		ordering = ('presbitero',)
		verbose_name = 'Presbitero Asignado'
		verbose_name_plural = 'Presbiteros Asignados'


# Mobiliarios (activos) de la iglesia
class Mobiliario(models.Model):
	mobiliario = models.CharField(max_length=100)
	cantidad = models.PositiveIntegerField()
	
	iglesia = models.ForeignKey(Iglesia)

	def __unicode__(self):
		return self.mobiliario

	class Meta:
		ordering = ('mobiliario',)
		verbose_name = 'Mobiliario'
		verbose_name_plural = 'Mobiliarios'


# Campos Blancos de iglesias
class CampoBlanco(models.Model):
	estatus_choices = (('A','Activo'), ('I','Inactivo'))

	direccion = models.TextField(max_length=100)
	telefono_contacto = models.CharField(max_length=50, null=True, blank=True)
	fecha_inicio = models.DateField(blank=True, null=True)
	observacion = models.CharField(max_length=100, null=True, blank=True)
	
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')
	encargado = models.ForeignKey(Miembro, null=True, blank=True)
	iglesia = models.ForeignKey(Iglesia)

	def __unicode__(self):
		return self.direccion

	class Meta:
		ordering = ('direccion',)
		verbose_name = 'Campo Blanco'
		verbose_name_plural = 'Campos Blancos'


# Cuerpo Oficial
class Cuerpo_Oficial(models.Model):
	desde = models.DateField(blank=True, null=True)
	hasta = models.DateField(blank=True, null=True)

	miembro = models.ForeignKey(Miembro)
	cargo = models.ForeignKey(Cargo)
	iglesia = models.ForeignKey(Iglesia)
	pastor = models.ForeignKey(Pastor)

	def __unicode__(self):
		return '%s %s' % (self.miembro.nombres, self.miembro.apellidos)

	class Meta:
		verbose_name = 'Cuerpo Oficial'
		verbose_name_plural = '2) Cuerpos Oficiales'

