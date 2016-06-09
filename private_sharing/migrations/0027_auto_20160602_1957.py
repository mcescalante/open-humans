# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0026_auto_20160328_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth2datarequestproject',
            name='redirect_url',
            field=models.CharField(help_text='The return URL for our "authorization code" OAuth2 grant\n        process. You can <a target="_blank" href="">read more about OAuth2\n        "authorization code" transactions here</a>.', max_length=256, verbose_name='Redirect URL'),
        ),
    ]