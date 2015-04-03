from django.contrib import admin

from .models import Estatus

class EstatusAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion','para',]
	list_editable = ('descripcion','para',)
	search_fields = ('descripcion','para',)

admin.site.register(Estatus,EstatusAdmin)
