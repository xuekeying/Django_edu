# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-15 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_video_learn_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='learn_time',
            field=models.CharField(default='', max_length=20, verbose_name='学习时长（分钟数）'),
        ),
    ]
