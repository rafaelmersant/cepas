from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import Miembro

class MiembrosView(TemplateView):

	template_name = 'miembros.html'