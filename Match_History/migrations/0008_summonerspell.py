# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0007_auto_20151114_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='summonerSpell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('summID', models.CharField(default=b'', max_length=20)),
                ('summurl', models.CharField(default=b'', max_length=50)),
            ],
        ),
    ]
