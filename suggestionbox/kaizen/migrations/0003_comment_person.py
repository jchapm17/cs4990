# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0002_auto_20151013_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
