# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0004_auto_20151114_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='ChampionID',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
