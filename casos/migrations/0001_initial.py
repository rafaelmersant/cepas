# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=500, blank=True)),
                ('estatus', models.CharField(max_length=1, choices=[(b'A', b'Abierto'), (b'C', b'Cerrado')])),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
