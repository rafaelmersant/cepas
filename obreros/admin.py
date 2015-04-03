from django.contrib import admin

from .models import Obrero
from iglesias.models import Iglesia


class ObreroAdmin(admin.ModelAdmin):
	list_display = ['anio_nombramiento','obrero','credencial','estatus','iglesia','pastor',]
	search_fields = ('obrero',)
	
admin.site.register(Obrero,ObreroAdmin)