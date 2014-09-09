from django.db import models

from miembros.models import Miembro
from pastores.models import Pastor
from presbiteros.models import Presbitero
from iglesias.models import Iglesia
from areas.models import Area
from conceptos_tesoreria.models import Concepto_Tesoreria


class Transaccion(models.Model):
	monto = models.DecimalField(max_digits=12, decimal_places=2)
	fecha_trans = models.DateTimeField()
	
	miembro 	= models.ForeignKey(Miembro)
	pastor 		= models.ForeignKey(Pastor)
	presbitero 	= models.ForeignKey(Presbitero)
	iglesia 	= models.ForeignKey(Iglesia)
	area 		= models.ForeignKey(Area)
	concepto 	= models.ForeignKey(Concepto_Tesoreria)
