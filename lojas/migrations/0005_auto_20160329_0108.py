# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 01:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0004_auto_20160329_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='status_id',
            new_name='status',
        ),
    ]
