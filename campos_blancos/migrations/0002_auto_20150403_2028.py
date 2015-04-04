# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
        ('campos_blancos', '0001_initial'),
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='campoblanco',
            name='encargado',
            field=models.ForeignKey(to='miembros.Miembro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campoblanco',
            name='iglesia',
            field=models.ForeignKey(to='iglesias.Iglesia'),
            preserve_default=True,
        ),
    ]
