# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0001_initial'),
        ('miembros', '0001_initial'),
        ('presbiteros', '0001_initial'),
        ('conceptos_tesoreria', '0001_initial'),
        ('iglesias', '__first__'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=12, decimal_places=2)),
                ('fecha_trans', models.DateTimeField()),
                ('area', models.ForeignKey(to='areas.Area')),
                ('concepto', models.ForeignKey(to='conceptos_tesoreria.Concepto_Tesoreria')),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
                ('miembro', models.ForeignKey(to='miembros.Miembro')),
                ('pastor', models.ForeignKey(to='pastores.Pastor')),
                ('presbitero', models.ForeignKey(to='presbiteros.Presbitero')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
