# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-03 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='宇宙著名', max_length=10, verbose_name='机构标签'),
        ),
    ]
