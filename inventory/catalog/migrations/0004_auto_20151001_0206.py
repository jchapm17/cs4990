# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20151001_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
