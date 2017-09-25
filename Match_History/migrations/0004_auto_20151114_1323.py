# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0003_champs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='champs',
            new_name='champion',
        ),
        migrations.RenameField(
            model_name='champion',
            old_name='ChampID',
            new_name='ChampImg',
        ),
    ]
