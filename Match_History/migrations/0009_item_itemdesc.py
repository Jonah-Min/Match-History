# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0008_summonerspell'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemDesc',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
