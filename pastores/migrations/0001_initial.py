# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('tipo_pastor', models.CharField(max_length=10, choices=[(b'Titular', b'Titular'), (b'NTitular', b'No Titular')])),
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
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
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
                ('pastor', models.ForeignKey(to='pastores.Pastor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
