from django.contrib import admin

from .models import Credencial

class CredencialAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

admin.site.register(Credencial,CredencialAdmin)
