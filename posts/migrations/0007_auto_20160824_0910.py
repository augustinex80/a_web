# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-24 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20160823_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tag_a',
        ),
    ]
