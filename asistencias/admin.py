from django.contrib import admin

from .models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ['id','reunion','obrero','motivo','pago','excusa_descrp',]
	list_editable = ('reunion','obrero','motivo','pago','excusa_descrp','obrero',)
	search_fields = ('reunion','motivo','excusa_descrp','obrero')

admin.site.register(Asistencia,AsistenciaAdmin)