from django.db import models

from administracion.models import Concepto_Tesoreria, Area, Pastor, Presbitero, Miembro, Iglesia


# Transaccion de un miembro hacia pago al concilio
class Transaccion(models.Model):
	monto = models.DecimalField(max_digits=12, decimal_places=2)
	fecha_trans = models.DateTimeField()
	
	miembro 	= models.ForeignKey(Miembro)
	pastor 		= models.ForeignKey(Pastor)
	presbitero 	= models.ForeignKey(Presbitero)
	iglesia 	= models.ForeignKey(Iglesia)
	area 		= models.ForeignKey(Area)
	concepto 	= models.ForeignKey(Concepto_Tesoreria)
