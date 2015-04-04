# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iglesias', '__first__'),
        ('areas', '0001_initial'),
        ('cargos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso_Miembro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso_descripcion', models.CharField(max_length=150, blank=True)),
                ('institucion', models.CharField(max_length=150, blank=True)),
                ('anio', models.PositiveIntegerField()),
                ('nivel', models.CharField(max_length=1, choices=[(b'L', b'Taller'), (b'T', b'Tecnico'), (b'U', b'Unversitario'), (b'O', b'Otro')])),
            ],
            options={
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
                ('habilidades', models.TextField(max_length=250, null=True, blank=True)),
                ('fecha_boda', models.DateField(null=True, blank=True)),
                ('nombre_de_pareja', models.CharField(max_length=100, null=True, blank=True)),
                ('pareja_cristiana', models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('iglesia', models.ForeignKey(blank=True, to='iglesias.Iglesia', null=True)),
            ],
            options={
                'ordering': ('nombres',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='curso_miembro',
            name='miembro',
            field=models.ForeignKey(to='miembros.Miembro'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Miembro_Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio_inicio', models.PositiveIntegerField()),
                ('anio_fin', models.PositiveIntegerField()),
                ('cargo', models.ForeignKey(to='cargos.Cargo')),
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrabajoRealizado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha', models.DateField()),
                ('area', models.ForeignKey(to='areas.Area')),
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
            ],
            options={
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
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
