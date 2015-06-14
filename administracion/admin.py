from django.contrib import admin

from cepas.actions import export_as_excel

from .models import Area, Tipo_Cargo, Cargo, Zona, Iglesia, Miembro, Miembro_Cargo, Curso_Miembro, \
					Miembro_Hijos, TrabajoRealizado, TrayectoriaMiembro, Pastor, Pastor_Asign, Presbitero, \
					Presbitero_Asign, Mobiliario, Cuerpo_Oficial, CampoBlanco, Miembro_Padres, Carrera, \
					Carrera_Miembro


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(Tipo_Cargo)
class Tipo_CargoAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion']
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion', 'tipo_cargo', 'area',]
	list_editable = ('descripcion', 'tipo_cargo', 'area',)
	search_fields = ('descripcion',)

class Presbitero_AsignInline(admin.StackedInline):
	model = Presbitero_Asign
	extra = 0

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion','Presbitero']
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

	inlines = [Presbitero_AsignInline,]

class CampoBlancoInline(admin.StackedInline):
	model = CampoBlanco
	extra = 0

class MobiliarioInline(admin.StackedInline):
	model = Mobiliario
	extra = 0

class Pastor_AsignInline(admin.StackedInline):
	model = Pastor_Asign
	extra = 0

@admin.register(Iglesia)
class IglesiaAdmin(admin.ModelAdmin):
	list_display = ['id','titulo_conciliar', 'titulo_local', 'zona', 'Pastor', 'fecha_fundacion', 'creadaPor', 'creadaFecha', 'modificadaPor', 'modificada']
	list_editable = ('titulo_conciliar', 'titulo_local', 'zona', 'fecha_fundacion')
	search_fields = ('titulo_conciliar', 'titulo_local')
	list_filter = ('zona',)
	actions = (export_as_excel,)

	inlines = [CampoBlancoInline, MobiliarioInline, Pastor_AsignInline]

	def save_model(self, request, obj, form, change):
		if obj.id == None:
			obj.creadaPor = request.user
		else:
			obj.modificadaPor = request.user

		obj.save()

class Miembro_CargoInline(admin.StackedInline):
	model = Miembro_Cargo
	extra = 0

class Miembro_HijosInline(admin.StackedInline):
	model = Miembro_Hijos
	extra = 0

class Miembro_PadresInline(admin.StackedInline):
	model = Miembro_Padres
	extra = 0

class Carrera_MiembroInline(admin.StackedInline):
	model = Carrera_Miembro
	extra = 0

class Curso_MiembroInline(admin.StackedInline):
	model = Curso_Miembro
	extra = 0

class TrabajoRealizadoInline(admin.StackedInline):
	model = TrabajoRealizado
	extra = 0

class TrayectoriaMiembroInline(admin.StackedInline):
	model = TrayectoriaMiembro
	extra = 0

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
	list_display = ['id','cedula_pasaporte', 'nombres', 'apellidos', 'sociedad', 'bautizado', 'iglesia', 'creadoFecha', \
					'creadoPor', 'modificado', 'modificadoPor']
	list_editable = ('nombres', 'apellidos', 'sociedad', 'bautizado', 'iglesia')
	search_fields = ('nombres', 'apellidos')
	
	list_filter = ('creadoPor', 'iglesia',)
	actions = (export_as_excel,)

	inlines = [Miembro_PadresInline, Miembro_HijosInline, Miembro_CargoInline, Carrera_MiembroInline,
				Curso_MiembroInline, TrabajoRealizadoInline, TrayectoriaMiembroInline, ]

	def save_model(self, request, obj, form, change):
		if obj.id == None:
			obj.creadoPor = request.user
		else:
			obj.modificadoPor = request.user

		obj.save()


@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
	list_display = ['id', 'miembro', 'Iglesia']
	search_fields = ('miembro',)

@admin.register(Presbitero)
class PresbiteroAdmin(admin.ModelAdmin):
	list_display = ['id','miembro',]
	search_fields = ('miembro',)


# @admin.register(Cuerpo_Oficial)
# class Cuerpo_OficialAdmin(admin.ModelAdmin):
# 	list_display = ['id','iglesia', 'pastor', 'miembro', 'cargo', 'desde', 'hasta']
# 	list_editable = ('desde', 'hasta', 'cargo')
# 	search_fields = ('miembro',)
# 	raw_id_fields = ('miembro',)
