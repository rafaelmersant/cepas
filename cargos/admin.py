from django.contrib import admin

from .models import Cargo

class CargoAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion','nivel','tipo_cargo','area',]
	list_editable = ('descripcion','nivel','tipo_cargo','area',)
	search_fields = ('descripcion',)

admin.site.register(Cargo,CargoAdmin)