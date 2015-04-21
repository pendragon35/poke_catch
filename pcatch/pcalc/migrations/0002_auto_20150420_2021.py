# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcalc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rates',
            old_name='poke_rate',
            new_name='bw_rate',
        ),
        migrations.AddField(
            model_name='rates',
            name='dp_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rates',
            name='xy_rate',
            field=models.IntegerField(default=0),
        ),
    ]
