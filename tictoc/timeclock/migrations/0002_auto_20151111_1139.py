# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punch',
            options={'ordering': ('-time_in',), 'verbose_name_plural': 'punches'},
        ),
    ]
