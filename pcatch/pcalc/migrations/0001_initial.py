# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poke_num', models.IntegerField(default=0)),
                ('poke_name', models.CharField(max_length=150)),
                ('poke_rate', models.IntegerField(default=0)),
            ],
        ),
    ]
