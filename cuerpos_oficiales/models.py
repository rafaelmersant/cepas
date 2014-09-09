from django.db import models

from iglesias.models import Iglesia
from pastores.models import Pastor
from miembros.models import Miembro
from cargos.models import Cargo

class Cuerpo_Oficial(models.Model):
	desde = models.DateField(blank=True)
	hasta = models.DateField(blank=True)

	miembro = models.ForeignKey(Miembro)
	cargo = models.ForeignKey(Cargo)
	iglesia = models.ForeignKey(Iglesia)
	pastor = models.ForeignKey(Pastor)
