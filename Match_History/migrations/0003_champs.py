# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0002_summoner_summonerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='champs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ChampionName', models.CharField(max_length=100)),
                ('ChampID', models.CharField(default=b'', max_length=20)),
            ],
        ),
    ]
