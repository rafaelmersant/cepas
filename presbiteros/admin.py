from django.contrib import admin

from .models import Presbitero

class PresbiteroAdmin(admin.ModelAdmin):
	list_display = ['id','miembro','estatus',]
	

admin.site.register(Presbitero,PresbiteroAdmin)