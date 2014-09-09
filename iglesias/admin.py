from django.contrib import admin

from .models import Iglesia
from zonas.models import Zona

# class ZonaSelf(admin.StackedInline):
# 	model = Zona
# 	extra = 1

class ListaSelf(admin.ModelAdmin):
	list_display = ('alias','titulo')
	search_fields = ('alias','titulo')
	# inlines = [ZonaSelf]


admin.site.register(Iglesia,ListaSelf)