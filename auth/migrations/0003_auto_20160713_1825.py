# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
        ('ct_auth', '0002_auto_20160413_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name', blank=True),
        ),
    ]
