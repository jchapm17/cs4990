# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='user',
            new_name='profile',
        ),
    ]
