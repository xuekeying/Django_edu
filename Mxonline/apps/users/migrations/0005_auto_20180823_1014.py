# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-23 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180804_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '忘记密码'), ('update_email', '修改邮箱')], max_length=10, verbose_name='验证码类型'),
        ),
    ]
