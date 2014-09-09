from django.contrib import admin

from .models import Obrero
from iglesias.models import Iglesia


class EnlaceInline(admin.StackedInline):
	model = Iglesia
	extra = 1
	
class ObreroSelf(admin.ModelAdmin):
	search_fields = ('Nombre',)
	raw_id_fields = ('iglesia_id')
	inlines = [EnlaceInline]

admin.site.register(Obrero)