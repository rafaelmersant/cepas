# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0001_initial'),
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuerpo_Oficial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desde', models.DateField(blank=True)),
                ('hasta', models.DateField(blank=True)),
                ('cargo', models.ForeignKey(to='cargos.Cargo')),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
            ],
            options={
                'verbose_name': 'Cuerpo Oficial',
                'verbose_name_plural': 'Cuerpos Oficiales',
            },
            bases=(models.Model,),
        ),
    ]
