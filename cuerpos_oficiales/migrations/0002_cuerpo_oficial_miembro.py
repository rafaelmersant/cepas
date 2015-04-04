# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
        ('cuerpos_oficiales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuerpo_oficial',
            name='miembro',
            field=models.ForeignKey(to='miembros.Miembro'),
            preserve_default=True,
        ),
    ]
