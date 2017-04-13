# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ct_auth', '0005_auto_20160713_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='publisher',
            field=models.BooleanField(default=False),
        ),
    ]
