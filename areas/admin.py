from django.contrib import admin

from .models import Area

class AreaAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

admin.site.register(Area,AreaAdmin)