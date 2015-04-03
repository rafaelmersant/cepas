from django.contrib import admin

from .models import Miembro

class MiembroAdmin(admin.ModelAdmin):
	list_display = ['id','nombres','apellidos','telefonos','direccion','correo','sexo','estado_civil','bautizado','iglesia','estatus']
	list_editable = ('nombres','apellidos','telefonos','direccion','correo','sexo','estado_civil','bautizado','iglesia','estatus',)
	search_fields = ('nombres','apellidos','cedula_pasaporte','nombre_de_pareja','iglesia',)

admin.site.register(Miembro,MiembroAdmin)