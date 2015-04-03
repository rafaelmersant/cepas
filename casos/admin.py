from django.contrib import admin

from .models import Caso

class CasoAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion','estatus','miembro','iglesia',]
	list_editable = ('descripcion','estatus','miembro','iglesia',)
	search_fields = ('descripcion','miembro','iglesia')

admin.site.register(Caso,CasoAdmin)
