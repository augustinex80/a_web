# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 13:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=datetime.datetime(2016, 8, 22, 13, 22, 53, 244218, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.get_pic_location),
        ),
    ]
