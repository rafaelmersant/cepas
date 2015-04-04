# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo', models.CharField(max_length=1, choices=[(b'P', b'Presente'), (b'A', b'Ausente'), (b'E', b'Excusa')])),
                ('pago', models.DecimalField(max_digits=8, decimal_places=2)),
                ('excusa_descrp', models.TextField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
