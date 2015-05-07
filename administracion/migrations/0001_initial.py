# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=70)),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Area',
                'verbose_name_plural': '4) Areas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampoBlanco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.TextField(max_length=100)),
                ('telefono_contacto', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('observacion', models.CharField(max_length=100, null=True, blank=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
            ],
            options={
                'ordering': ('direccion',),
                'verbose_name': 'Campo Blanco',
                'verbose_name_plural': 'Campos Blancos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
                ('area', models.ForeignKey(to='administracion.Area')),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Cargo',
                'verbose_name_plural': '6) Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=500, blank=True)),
                ('estatus', models.CharField(max_length=1, choices=[(b'A', b'Abierto'), (b'C', b'Cerrado')])),
            ],
            options={
                'ordering': ('miembro', 'descripcion'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Concepto_Tesoreria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=1, choices=[(b'D', b'Debito'), (b'C', b'Credito')])),
            ],
            options={
                'ordering': ('descripcion',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuerpo_Oficial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desde', models.DateField(null=True, blank=True)),
                ('hasta', models.DateField(null=True, blank=True)),
                ('cargo', models.ForeignKey(to='administracion.Cargo')),
            ],
            options={
                'verbose_name': 'Cuerpo Oficial',
                'verbose_name_plural': '2) Cuerpos Oficiales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso_Miembro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso_descripcion', models.CharField(max_length=150, blank=True)),
                ('institucion', models.CharField(max_length=150, blank=True)),
                ('anio_inicio', models.PositiveIntegerField(null=True, verbose_name=b'A\xc3\xb1o Inicio', blank=True)),
                ('anio_fin', models.PositiveIntegerField(null=True, verbose_name=b'A\xc3\xb1o Fin', blank=True)),
                ('nivel', models.CharField(max_length=1, choices=[(b'L', b'Taller'), (b'T', b'Tecnico'), (b'U', b'Unversitario'), (b'O', b'Otro')])),
                ('clasificacion', models.CharField(blank=True, max_length=1, null=True, choices=[(b'E', b'Eclesiastico'), (b'S', b'Secular')])),
            ],
            options={
                'ordering': ('miembro', 'curso_descripcion'),
                'verbose_name': 'Curso de Miembro',
                'verbose_name_plural': 'Cursos de Miembros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Iglesia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_conciliar', models.CharField(max_length=150)),
                ('titulo_local', models.CharField(max_length=150, blank=True)),
                ('direccion', models.TextField(max_length=200, blank=True)),
                ('telefono_contacto', models.CharField(max_length=50, blank=True)),
                ('tipo_iglesia', models.CharField(default=b'M', max_length=1, blank=True, choices=[(b'M', b'Miembro'), (b'A', b'Asociada')])),
                ('denominacion_origen', models.CharField(max_length=100, blank=True)),
                ('fecha_fundacion', models.DateField(null=True, blank=True)),
                ('local', models.CharField(blank=True, max_length=1, choices=[(b'P', b'Propio'), (b'A', b'Alquilado'), (b'D', b'Desconocido')])),
                ('observacion', models.TextField(max_length=100, blank=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('creadaFecha', models.DateTimeField(auto_now_add=True)),
                ('modificada', models.DateTimeField(auto_now=True)),
                ('creadaPor', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificadaPor', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('titulo_conciliar',),
                'verbose_name': 'Iglesia',
                'verbose_name_plural': '1) Iglesias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula_pasaporte', models.CharField(max_length=13, null=True, verbose_name=b'Cedula o Pasaporte', blank=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40, null=True, blank=True)),
                ('telefonos', models.CharField(max_length=50, null=True, blank=True)),
                ('direccion', models.CharField(max_length=150, null=True, blank=True)),
                ('correo', models.CharField(max_length=50, null=True, blank=True)),
                ('sexo', models.CharField(max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')])),
                ('estado_civil', models.CharField(max_length=1, null=True, choices=[(b'S', b'Soltero(a)'), (b'C', b'Casado(a)')])),
                ('dia_nacimiento', models.PositiveIntegerField(null=True, blank=True)),
                ('mes_nacimiento', models.CharField(blank=True, max_length=2, null=True, choices=[(b'01', b'Enero'), (b'02', b'Febrero'), (b'03', b'Marzo'), (b'04', b'Abril'), (b'05', b'Mayo'), (b'06', b'Junio'), (b'07', b'Julio'), (b'08', b'Agosto'), (b'09', b'Septiembre'), (b'10', b'Octubre'), (b'11', b'Noviembre'), (b'12', b'Diciembre')])),
                ('anio_nacimiento', models.PositiveIntegerField(null=True, verbose_name=b'A\xc3\xb1o nacimiento', blank=True)),
                ('sociedad', models.CharField(blank=True, max_length=1, null=True, choices=[(b'D', b'Damas'), (b'C', b'Caballeros'), (b'J', b'Jovenes'), (b'A', b'Adolescentes'), (b'N', b'Ni\xc3\xb1os')])),
                ('bautizado', models.CharField(default=b'N', max_length=2, null=True, blank=True, choices=[(b'N', b'NO'), (b'S', b'SI')])),
                ('fecha_bautismo', models.DateField(null=True, blank=True)),
                ('fecha_profesionfe', models.DateField(null=True, blank=True)),
                ('tipo_miembro', models.CharField(default=b'M', max_length=1, null=True, choices=[(b'M', b'Miembro'), (b'A', b'Asociado')])),
                ('iglesia_procedencia', models.CharField(max_length=100, null=True, blank=True)),
                ('habilidades', models.TextField(max_length=250, null=True, verbose_name=b'Habilidades (separadas por coma)', blank=True)),
                ('fecha_boda', models.DateField(null=True, blank=True)),
                ('nombre_de_pareja', models.CharField(max_length=100, null=True, blank=True)),
                ('pareja_cristiana', models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('foto', models.FileField(null=True, upload_to=b'cepas/static/media/fotos/', blank=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('creadaFecha', models.DateTimeField(auto_now_add=True)),
                ('modificada', models.DateTimeField(auto_now=True)),
                ('creadaPor', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('iglesia', models.ForeignKey(blank=True, to='administracion.Iglesia', null=True)),
                ('modificadaPor', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('nombres',),
                'verbose_name': 'Miembro',
                'verbose_name_plural': '3) Miembros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Miembro_Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio_inicio', models.PositiveIntegerField(null=True, verbose_name=b'A\xc3\xb1o Inicio', blank=True)),
                ('anio_fin', models.PositiveIntegerField(default=9999, null=True, verbose_name=b'A\xc3\xb1o Fin', blank=True)),
                ('cargo', models.ForeignKey(to='administracion.Cargo')),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'ordering': ('miembro',),
                'verbose_name': 'Cargo de Miembro',
                'verbose_name_plural': 'Cargos de Miembro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Miembro_Hijos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreHijo', models.CharField(max_length=80, null=True, verbose_name=b'Nombre de Hijo(a)', blank=True)),
                ('fechaNacimiento', models.DateField(null=True, verbose_name=b'Fecha de Nacimiento', blank=True)),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'verbose_name': 'Hijo de Miembro',
                'verbose_name_plural': 'Hijos de Miembro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Miembro_Padres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('madre', models.CharField(max_length=80, null=True, verbose_name=b'Madre (o tutora)', blank=True)),
                ('madreCristiana', models.CharField(default=b'S', max_length=1, verbose_name=b'Madre (o tutora) Cristiana?', choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('padre', models.CharField(max_length=80, null=True, verbose_name=b'Padre (o tutor)', blank=True)),
                ('padreCristiano', models.CharField(default=b'S', max_length=1, verbose_name=b'Padre (o tutor) Cristiano?', choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'verbose_name': 'Padres de Miembros (Obligatorio para ni\xf1os y/o adolescentes',
                'verbose_name_plural': 'Padres de Miembros (Obligatorio para ni\xf1os y/o adolescentes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mobiliario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobiliario', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField()),
                ('iglesia', models.ForeignKey(to='administracion.Iglesia')),
            ],
            options={
                'ordering': ('mobiliario',),
                'verbose_name': 'Mobiliario',
                'verbose_name_plural': 'Mobiliarios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('tipo_pastor', models.CharField(max_length=10, choices=[(b'Titular', b'Titular'), (b'NTitular', b'No Titular')])),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'verbose_name': 'Pastor',
                'verbose_name_plural': 'Pastores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pastor_Asign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_fin', models.DateField(default=b'31/12/9999', null=True, blank=True)),
                ('iglesia', models.ForeignKey(to='administracion.Iglesia')),
                ('pastor', models.ForeignKey(to='administracion.Pastor')),
            ],
            options={
                'verbose_name': 'Pastor asignado',
                'verbose_name_plural': 'Pastores Asignados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presbitero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'ordering': ('miembro',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presbitero_Asign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_fin', models.DateField(default=b'31/12/9999', null=True, blank=True)),
                ('presbitero', models.ForeignKey(to='administracion.Presbitero')),
            ],
            options={
                'ordering': ('presbitero',),
                'verbose_name': 'Presbitero Asignado',
                'verbose_name_plural': 'Presbiteros Asignados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Tipo de Cargo',
                'verbose_name_plural': '5) Tipos de Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrabajoRealizado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha', models.DateField()),
                ('area', models.ForeignKey(to='administracion.Area')),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'ordering': ('miembro', 'descripcion'),
                'verbose_name': 'Trabajo Realizado',
                'verbose_name_plural': 'Trabajos Realizados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrayectoriaMiembro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha', models.DateField()),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('miembro', models.ForeignKey(to='administracion.Miembro')),
            ],
            options={
                'ordering': ('miembro', 'fecha'),
                'verbose_name': 'Trayectoria Miembro',
                'verbose_name_plural': 'Trayectorias de Miembros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('provincia', models.CharField(max_length=2, choices=[(b'1', b'Azua'), (b'2', b'Bahoruco'), (b'3', b'Barahona'), (b'4', b'Dajabon'), (b'5', b'Distrito Nacional'), (b'6', b'Duarte'), (b'7', b'Elias Pi\xc3\xb1a'), (b'8', b'El Seibo'), (b'9', b'Espaillat'), (b'10', b'Hato Mayor'), (b'11', b'Hermanas Mirabal'), (b'12', b'Independencia'), (b'13', b'La Altagracia'), (b'14', b'La Romana'), (b'15', b'La Vega'), (b'16', b'Maria Trinidad Sanchez'), (b'17', b'Monse\xc3\xb1or Nouel'), (b'18', b'Monte Cristi'), (b'19', b'Monte Plata'), (b'20', b'Pedernales'), (b'21', b'Peravia'), (b'22', b'Puerto Plata'), (b'23', b'Saman\xc3\xa1'), (b'24', b'Sanchez Ramirez'), (b'25', b'San Cristobal'), (b'26', b'San Jose de Ocoa'), (b'27', b'San Juan'), (b'28', b'San Pedro de Macoris'), (b'29', b'Santiago'), (b'30', b'Santiago Rodriguez'), (b'31', b'Santo Domingo'), (b'32', b'Valverde'), (b'33', b'Internacional')])),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name_plural': '7) Zonas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='presbitero_asign',
            name='zona',
            field=models.ForeignKey(to='administracion.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iglesia',
            name='zona',
            field=models.ForeignKey(blank=True, to='administracion.Zona', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso_miembro',
            name='miembro',
            field=models.ForeignKey(to='administracion.Miembro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuerpo_oficial',
            name='iglesia',
            field=models.ForeignKey(to='administracion.Iglesia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuerpo_oficial',
            name='miembro',
            field=models.ForeignKey(to='administracion.Miembro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuerpo_oficial',
            name='pastor',
            field=models.ForeignKey(to='administracion.Pastor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caso',
            name='iglesia',
            field=models.ForeignKey(to='administracion.Iglesia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caso',
            name='miembro',
            field=models.ForeignKey(to='administracion.Miembro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='tipo_cargo',
            field=models.ForeignKey(to='administracion.Tipo_Cargo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campoblanco',
            name='encargado',
            field=models.ForeignKey(blank=True, to='administracion.Miembro', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campoblanco',
            name='iglesia',
            field=models.ForeignKey(to='administracion.Iglesia'),
            preserve_default=True,
        ),
    ]
