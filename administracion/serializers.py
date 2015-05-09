# SERIALIZERS -- Administracion

from rest_framework import serializers

from .models import Miembro

# Listado de Miembros
class MiembrosSerializer(serializers.HyperlinkedModelSerializer):
	iglesia = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Miembro
		fields = ('id','nombres','apellidos','iglesia',)
		ordering = ('nombres', 'apellidos',)