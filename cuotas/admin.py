from django.contrib import admin

from .models import Cuota

class CuotaAdmin(admin.ModelAdmin):
	list_display = ['id','concepto','clave','cuota',]
	list_editable = ('concepto','clave','cuota',)
	search_fields = ('concepto',)

admin.site.register(Cuota,CuotaAdmin)
