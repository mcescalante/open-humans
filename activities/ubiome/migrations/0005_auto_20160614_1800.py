# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubiome', '0004_auto_20160316_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubiomesample',
            name='sample_date',
        ),
        migrations.RemoveField(
            model_name='ubiomesample',
            name='sample_type',
        ),
    ]