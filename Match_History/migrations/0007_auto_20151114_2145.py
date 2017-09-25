# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match_History', '0006_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='item',
        ),
    ]
