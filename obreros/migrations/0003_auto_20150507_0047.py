# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obreros', '0002_auto_20150507_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrero',
            name='creadoFecha',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obrero',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
