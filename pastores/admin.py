from django.contrib import admin

from .models import Pastor

class PastorAdmin(admin.ModelAdmin):
	list_display = ['id','miembro','estatus','tipo_pastor','fecha',]
	list_editable = ('miembro','estatus','tipo_pastor','fecha',)
	search_fields = ('miembro',)

admin.site.register(Pastor,PastorAdmin)
