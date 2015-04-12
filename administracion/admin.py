from django.contrib import admin

from .models import Area, Tipo_Cargo, Cargo, Zona, Iglesia, Miembro, Miembro_Cargo, Curso_Miembro, \
					TrabajoRealizado, TrayectoriaMiembro, Pastor, Pastor_Asign, Presbitero, \
					Presbitero_Asign, Mobiliario, Cuerpo_Oficial, CampoBlanco 


@admin.register(Area)
class AreaDmin(admin.ModelAdmin):
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

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

class CampoBlancoInline(admin.StackedInline):
	model = CampoBlanco
	extra = 1

class MobiliarioInline(admin.StackedInline):
	model = Mobiliario
	extra = 1

@admin.register(Iglesia)
class IglesiaAdmin(admin.ModelAdmin):
	list_display = ['id','titulo_conciliar', 'titulo_local', 'zona', 'telefono_contacto', 'fecha_fundacion']
	list_editable = ('titulo_conciliar', 'titulo_local', 'zona', 'telefono_contacto', 'fecha_fundacion')
	search_fields = ('titulo_conciliar', 'titulo_local')
	list_filter = ('zona',)

	inlines = [CampoBlancoInline, MobiliarioInline]

class Miembro_CargoInline(admin.StackedInline):
	model = Miembro_Cargo
	extra = 1

class Curso_MiembroInline(admin.StackedInline):
	model = Curso_Miembro
	extra = 1

class TrabajoRealizadoInline(admin.StackedInline):
	model = TrabajoRealizado
	extra = 1

class TrayectoriaMiembroInline(admin.StackedInline):
	model = TrayectoriaMiembro
	extra = 1

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
	list_display = ['id','cedula_pasaporte', 'nombres', 'apellidos', 'sociedad', 'bautizado', 'iglesia']
	list_editable = ('nombres', 'apellidos', 'sociedad', 'bautizado', 'iglesia')
	search_fields = ('nombres', 'apellidos')

	inlines = [Miembro_CargoInline, Curso_MiembroInline, TrabajoRealizadoInline, TrayectoriaMiembroInline, ]


@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
	list_display = ['id','miembro',]
	search_fields = ('miembro',)

@admin.register(Pastor_Asign)
class Pastor_AsignAdmin(admin.ModelAdmin):
	list_display = ['id','pastor', 'iglesia', 'fecha_inicio', 'fecha_fin']
	list_editable = ('fecha_inicio', 'fecha_fin',)
	search_fields = ('pastor',)

@admin.register(Presbitero)
class PresbiteroAdmin(admin.ModelAdmin):
	list_display = ['id','miembro',]
	search_fields = ('miembro',)

@admin.register(Presbitero_Asign)
class Presbitero_AsignAdmin(admin.ModelAdmin):
	list_display = ['id','presbitero', 'zona', 'fecha_inicio', 'fecha_fin']
	list_editable = ('fecha_inicio', 'fecha_fin',)
	search_fields = ('presbitero',)


@admin.register(Cuerpo_Oficial)
class Cuerpo_OficialAdmin(admin.ModelAdmin):
	list_display = ['id','iglesia', 'pastor', 'miembro', 'cargo', 'desde', 'hasta']
	list_editable = ('desde', 'hasta', 'cargo')
	search_fields = ('miembro',)
	raw_id_fields = ('miembro',)
