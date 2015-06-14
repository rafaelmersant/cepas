from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from cepas.views import LoginRequiredMixin

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

	def get(self, request, nombreApellido=None):

		if nombreApellido == None:
			miembros = Miembro.objects.all()
		else: 
			miembros = Miembro.objects.filter( Q(nombres__contains=nombreApellido.upper()) | Q(apellidos__contains=nombreApellido.upper()))

		response = self.serializer_class(miembros, many=True)
		return Response(response.data)


# Digitacion de usuarios (Modificados)
class GrupoDigitadores(LoginRequiredMixin, DetailView):

	def get(self, request, *args, **kwargs):

		return self.json_to_response()
		
	def json_to_response(self):
		data = list()
		registros = Miembro.objects.raw('SELECT m.id, count(0) as cantidadTotal, \
											i.titulo_conciliar, \
											u.username \
										FROM administracion_miembro m \
										INNER JOIN auth_user u on u.id = m.modificadoPor_id \
										LEFT OUTER JOIN administracion_iglesia i on i.id = m.iglesia_id \
										GROUP BY iglesia_id, modificadoPor_id \
										HAVING cantidadTotal > 1 and username <> \'cepas\' \
										ORDER BY cantidadTotal desc')

		for registro in registros:
			data.append({
				'cantidad': registro.cantidadTotal,
				'titulo_conciliar': registro.titulo_conciliar,
				'username': registro.username,
			})

		return JsonResponse(data, safe=False)


# Digitacion de usuarios (Creados)
class GrupoDigitadoresCreados(LoginRequiredMixin, DetailView):

	def get(self, request, *args, **kwargs):

		return self.json_to_response()
		
	def json_to_response(self):
		data = list()
		registros = Miembro.objects.raw('SELECT m.id, count(0) as cantidadTotal, \
											i.titulo_conciliar, \
											u.username \
										FROM administracion_miembro m \
										INNER JOIN auth_user u on u.id = m.creadoPor_id \
										LEFT OUTER JOIN administracion_iglesia i on i.id = m.iglesia_id \
										GROUP BY iglesia_id, creadoPor_id \
										HAVING cantidadTotal > 1 and username <> \'cepas\' \
										ORDER BY cantidadTotal desc')

		for registro in registros:
			data.append({
				'cantidad': registro.cantidadTotal,
				'titulo_conciliar': registro.titulo_conciliar,
				'username': registro.username,
			})

		return JsonResponse(data, safe=False)