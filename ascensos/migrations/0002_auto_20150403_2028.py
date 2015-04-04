# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ascensos', '0001_initial'),
        ('credenciales', '0001_initial'),
        ('obreros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ascenso',
            name='obrero',
            field=models.ForeignKey(to='obreros.Obrero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ascenso',
            name='rango_nuevo',
            field=models.ForeignKey(to='credenciales.Credencial'),
            preserve_default=True,
        ),
    ]
