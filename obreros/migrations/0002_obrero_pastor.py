# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0001_initial'),
        ('obreros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obrero',
            name='pastor',
            field=models.ForeignKey(to='pastores.Pastor'),
            preserve_default=True,
        ),
    ]
