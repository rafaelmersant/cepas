from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import Miembro


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