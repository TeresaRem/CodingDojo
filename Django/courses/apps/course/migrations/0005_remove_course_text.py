# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 00:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20170202_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='text',
        ),
    ]