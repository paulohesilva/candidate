# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ct_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_username',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_social',
            field=models.BooleanField(default=False),
        ),
    ]
