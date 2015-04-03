from django.contrib import admin

from .models import CampoBlanco

class CampoBlancoAdmin(admin.ModelAdmin):
	list_display = ['id','direccion','telefono_contacto','fecha_inicio','observacion','estatus','encargado','iglesia']
	list_editable = ('direccion','telefono_contacto','fecha_inicio','observacion','estatus','encargado','iglesia')
	list_filter = ('iglesia',)
	search_fields = ('direccion','telefono_contacto','iglesia')

admin.site.register(CampoBlanco,CampoBlancoAdmin)