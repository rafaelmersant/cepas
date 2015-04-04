# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase_reunion', models.CharField(max_length=1, choices=[(b'O', b'Ordinaria'), (b'E', b'Extraordinaria')])),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=150, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Reunion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('observacion', models.TextField(max_length=350)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reunion',
            name='tipo_reunion',
            field=models.ForeignKey(to='reuniones.Tipo_Reunion'),
            preserve_default=True,
        ),
    ]
