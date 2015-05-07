# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obreros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Presente'), (b'A', b'Ausente'), (b'E', b'Excusa')])),
                ('pago', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('excusa_descrp', models.TextField(max_length=200, null=True, blank=True)),
                ('obrero', models.ForeignKey(to='obreros.Obrero')),
            ],
            options={
                'ordering': ('obrero',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase_reunion', models.CharField(default=b'O', max_length=1, choices=[(b'O', b'Ordinaria'), (b'E', b'Extraordinaria')])),
                ('fecha', models.DateField(unique=True)),
                ('lugar', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('fecha',),
                'verbose_name': 'Reunion',
                'verbose_name_plural': 'Reuniones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Reunion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
                ('observacion', models.TextField(max_length=350, null=True, blank=True)),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Tipo de Reunion',
                'verbose_name_plural': 'Tipos de Reuniones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reunion',
            name='tipo_reunion',
            field=models.ForeignKey(to='reuniones.Tipo_Reunion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asistencia',
            name='reunion',
            field=models.ForeignKey(to='reuniones.Reunion'),
            preserve_default=True,
        ),
    ]
