# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 05:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_auth', '0006_auto_20161227_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialauth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_auth', to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
    ]
