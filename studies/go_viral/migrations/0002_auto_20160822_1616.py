# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 16:16


import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go_viral', '0001_squashed_0011_auto_20160212_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
