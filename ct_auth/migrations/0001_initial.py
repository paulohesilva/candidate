# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import ct_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('full_name', models.CharField(blank=True, verbose_name='full name', max_length=50)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image_field', models.ImageField(blank=True, upload_to=ct_auth.models.User.upload_image_profile, null=True)),
                ('username', models.CharField(blank=True, unique=True, null=True, max_length=255)),
                ('confirm_username', models.BooleanField(default=False)),
                ('is_social', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, null=True, max_length=50)),
                ('publisher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'users',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name': 'user',
                'ordering': ('full_name',),
                'abstract': False,
            },
            managers=[
                ('objects', ct_auth.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryKey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('key', models.TextField(max_length=40)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sos_recovery_key',
            },
        ),
    ]
