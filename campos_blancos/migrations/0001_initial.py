# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampoBlanco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.TextField(max_length=200, blank=True)),
                ('telefono_contacto', models.CharField(max_length=50, blank=True)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('observacion', models.CharField(max_length=100, blank=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
