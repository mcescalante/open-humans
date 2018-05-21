# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 17:19


import common.fields
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_import', '0001_squashed_0020_auto_20160729_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='go_viral', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name': 'GoViral user data', 'verbose_name_plural': 'GoViral user data'},
        ),
        migrations.AddField(
            model_name='userdata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
