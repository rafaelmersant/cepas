from django.contrib import admin

from .models import Cuerpo_Oficial

class CuerpoOficialAdmin(admin.ModelAdmin):
	list_display = ['id','desde','hasta','miembro','cargo','iglesia','pastor',]
	list_editable = ('desde','hasta','miembro','cargo','iglesia','pastor')
	search_fields = ('miembro','cargo','iglesia','pastor')

admin.site.register(Cuerpo_Oficial,CuerpoOficialAdmin)
