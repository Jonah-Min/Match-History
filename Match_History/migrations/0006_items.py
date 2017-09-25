# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0005_champion_championid'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemName', models.CharField(max_length=100)),
                ('itemID', models.CharField(default=b'', max_length=20)),
                ('itemUrl', models.CharField(default=b'', max_length=20)),
            ],
        ),
    ]
