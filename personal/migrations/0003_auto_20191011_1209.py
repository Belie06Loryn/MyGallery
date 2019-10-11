# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20191010_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='loca',
        ),
        migrations.AddField(
            model_name='photos',
            name='loca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.Location'),
        ),
    ]
