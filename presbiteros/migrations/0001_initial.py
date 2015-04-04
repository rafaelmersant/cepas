# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
        ('zonas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presbitero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presbitero_Asign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('presbitero', models.ForeignKey(to='presbiteros.Presbitero')),
                ('zona', models.ForeignKey(to='zonas.Zona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
