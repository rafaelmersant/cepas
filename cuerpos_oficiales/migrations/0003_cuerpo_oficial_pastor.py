# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpos_oficiales', '0002_cuerpo_oficial_miembro'),
        ('pastores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuerpo_oficial',
            name='pastor',
            field=models.ForeignKey(to='pastores.Pastor'),
            preserve_default=True,
        ),
    ]
