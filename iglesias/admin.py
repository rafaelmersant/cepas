from django.contrib import admin

from .models import Iglesia
from zonas.models import Zona

# class ZonaSelf(admin.StackedInline):
# 	model = Zona
# 	extra = 1

class IglesiaAdmin(admin.ModelAdmin):
	list_display = ['zona','titulo_conciliar','titulo_local','direccion','telefono_contacto','tipo_iglesia','fecha_fundacion','estatus']
	search_fields = ('titulo_conciliar','titulo_local')
	list_editable = ('zona','titulo_conciliar','titulo_local','direccion','telefono_contacto','tipo_iglesia','fecha_fundacion','estatus')

admin.site.register(Iglesia,IglesiaAdmin)