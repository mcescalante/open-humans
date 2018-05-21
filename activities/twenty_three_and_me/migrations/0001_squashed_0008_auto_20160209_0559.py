# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 17:58


import common.fields
import data_import.utils
from django.conf import settings
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
                ('user', common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name=b'23andme', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=common.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='twenty_three_and_me', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name': '23andMe user data', 'verbose_name_plural': '23andMe user data'},
        ),
        migrations.AddField(
            model_name='userdata',
            name='genome_file',
            field=models.FileField(max_length=1024, null=True, upload_to=data_import.utils.get_upload_path),
        ),
    ]
