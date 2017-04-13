# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ct_auth.models
from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ct_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('name', models.CharField(null=True, max_length=15, unique=True)),
                ('cpf', models.CharField(null=True, max_length=15, unique=True)),
                ('rg', models.IntegerField(null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('lattes', models.URLField(null=True, blank=True)),
                ('about', models.TextField(null=True, blank=True, max_length=10000)),
            ],
            options={
                'abstract': False,
            },
            bases=('ct_auth.user',),
            managers=[
                ('objects', ct_auth.models.CustomUserManager()),
            ],
        ),
    ]
