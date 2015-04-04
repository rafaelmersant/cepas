# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto_Tesoreria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=1, choices=[(b'D', b'Debito'), (b'C', b'Credito')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
