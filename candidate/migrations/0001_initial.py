# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, unique=True, max_length=15)),
                ('cpf', models.CharField(null=True, unique=True, max_length=15)),
                ('rg', models.IntegerField(null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('lattes', models.URLField(null=True, blank=True)),
                ('about', models.TextField(null=True, blank=True, max_length=10000)),
            ],
        ),
    ]
