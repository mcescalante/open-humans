# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-02 19:32


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0005_auto_20160926_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequestproject',
            name='info_url',
            field=models.URLField(blank=True, verbose_name='URL for general information about your project'),
        ),
    ]
