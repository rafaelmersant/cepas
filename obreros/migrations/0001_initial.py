# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
        ('credenciales', '0001_initial'),
        ('iglesias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obrero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio_nombramiento', models.PositiveIntegerField()),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('credencial', models.ForeignKey(to='credenciales.Credencial')),
                ('iglesia', models.ForeignKey(to='iglesias.Iglesia')),
                ('obrero', models.ForeignKey(to='miembros.Miembro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
