# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0001_initial'),
        ('reuniones', '0001_initial'),
        ('obreros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='obrero',
            field=models.ForeignKey(to='obreros.Obrero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asistencia',
            name='reunion',
            field=models.ForeignKey(to='reuniones.Reunion'),
            preserve_default=True,
        ),
    ]
