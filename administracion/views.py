from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.db.models import Q

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Miembro

from .serializers import MiembrosSerializer


# Vista para Iglesias
class IglesiasView(TemplateView):

	template_name = 'iglesias.html'


# Vista para Miembros
class MiembrosView(TemplateView):

	template_name = 'miembros.html'


# Vista para Pastores
class PastoresView(TemplateView):

	template_name = 'pastores.html'


# Vista para Presbiteros
class PresbiterosView(TemplateView):

	template_name = 'presbiteros.html'


# Vista para Obreros
class ObrerosView(TemplateView):

	template_name = 'obreros.html'


# Todos los miembros o por nombre
class MiembrosByNombreApellido(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

	serializer_class = MiembrosSerializer

	def get(self, request, nombreApellido=None,):
		if nombreApellido == None:
			miembros = Miembro.objects.all()
		else:
			miembros = Miembro.objects.filter( Q(nombres__contains=nombreApellido.upper()) | Q(apellidos__contains=nombreApellido.upper()))

		response = self.serializer_class(miembros, many=True)
		return Response(response.data)