# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiliario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobiliario', models.CharField(max_length=100, blank=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
