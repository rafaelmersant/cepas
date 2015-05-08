# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=70, verbose_name=b'Carrera Universitaria')),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ('descripcion',), 'verbose_name': 'Area', 'verbose_name_plural': '3) Areas'},
        ),
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ('descripcion',), 'verbose_name': 'Cargo', 'verbose_name_plural': '5) Cargos'},
        ),
        migrations.AlterModelOptions(
            name='miembro',
            options={'ordering': ('nombres',), 'verbose_name': 'Miembro', 'verbose_name_plural': '2) Miembros'},
        ),
        migrations.AlterModelOptions(
            name='tipo_cargo',
            options={'ordering': ('descripcion',), 'verbose_name': 'Tipo de Cargo', 'verbose_name_plural': '4) Tipos de Cargos'},
        ),
        migrations.AlterModelOptions(
            name='zona',
            options={'ordering': ('descripcion',), 'verbose_name_plural': '6) Zonas'},
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='creadaFecha',
            new_name='creadoFecha',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='creadaPor',
            new_name='creadoPor',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='modificada',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='miembro',
            old_name='modificadaPor',
            new_name='modificadoPor',
        ),
        migrations.AddField(
            model_name='miembro',
            name='carrera',
            field=models.ForeignKey(blank=True, to='administracion.Carrera', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miembro',
            name='anio_nacimiento',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Agno nacimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='miembro',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'Soltero(a)'), (b'C', b'Casado(a)'), (b'V', b'Viudo(a)'), (b'U', b'Union Libre'), (b'O', b'Otro')]),
            preserve_default=True,
        ),
    ]
