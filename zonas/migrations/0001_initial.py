# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=80)),
                ('Provincia', models.CharField(max_length=2, choices=[(b'1', b'Azua'), (b'2', b'Bahoruco'), (b'3', b'Barahona'), (b'4', b'Dajabon'), (b'5', b'Distrito Nacional'), (b'6', b'Duarte'), (b'7', b'Elias Pi\xc3\xb1a'), (b'8', b'El Seibo'), (b'9', b'Espaillat'), (b'10', b'Hato Mayor'), (b'11', b'Hermanas Mirabal'), (b'12', b'Independencia'), (b'13', b'La Altagracia'), (b'14', b'La Romana'), (b'15', b'La Vega'), (b'16', b'Maria Trinidad Sanchez'), (b'17', b'Monse\xc3\xb1or Nouel'), (b'18', b'Monte Cristi'), (b'19', b'Monte Plata'), (b'20', b'Pedernales'), (b'21', b'Peravia'), (b'22', b'Puerto Plata'), (b'23', b'Saman\xc3\xa1'), (b'24', b'Sanchez Ramirez'), (b'25', b'San Cristobal'), (b'26', b'San Jose de Ocoa'), (b'27', b'San Juan'), (b'28', b'San Pedro de Macoris'), (b'29', b'Santiago'), (b'30', b'Santiago Rodriguez'), (b'31', b'Santo Domingo'), (b'32', b'Valverde'), (b'33', b'Internacional')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
