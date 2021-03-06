# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 19:37
from __future__ import unicode_literals

import common.fields
import data_import.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(max_length=1024, null=True, upload_to=data_import.utils.get_upload_path)),
                ('user', common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mpower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'mPower user data',
                'verbose_name_plural': 'mPower user data',
            },
        ),
    ]
