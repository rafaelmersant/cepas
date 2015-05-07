# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ascenso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.PositiveIntegerField(verbose_name=b'A\xc3\xb1o')),
            ],
            options={
                'ordering': ('obrero', '-anio'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Credencial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'verbose_name': 'Credencial',
                'verbose_name_plural': 'Credenciales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=3, null=True, blank=True)),
                ('cuota', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
                'ordering': ('concepto',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Obrero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio_nombramiento', models.PositiveIntegerField(verbose_name=b'A\xc3\xb1o nombramiento')),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('credencial', models.ForeignKey(to='obreros.Credencial')),
                ('iglesia', models.ForeignKey(to='administracion.Iglesia')),
                ('obrero', models.ForeignKey(to='administracion.Miembro', unique=True)),
                ('pastor', models.ForeignKey(to='administracion.Pastor')),
            ],
            options={
                'ordering': ('obrero', 'anio_nombramiento'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ascenso',
            name='obrero',
            field=models.ForeignKey(to='obreros.Obrero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ascenso',
            name='rango_nuevo',
            field=models.ForeignKey(to='obreros.Credencial'),
            preserve_default=True,
        ),
    ]
