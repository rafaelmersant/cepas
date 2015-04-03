from django.contrib import admin

from .models import Mobiliario

class MobiliarioAdmin(admin.ModelAdmin):
	list_display = ['id','mobiliario','cantidad','iglesia',]
	list_editable = ('mobiliario','cantidad','iglesia',)
	search_fields = ('mobiliario','iglesia',)

admin.site.register(Mobiliario,MobiliarioAdmin)