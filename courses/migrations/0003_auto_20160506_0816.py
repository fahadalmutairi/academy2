# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160506_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject_description',
            new_name='description',
        ),
    ]
