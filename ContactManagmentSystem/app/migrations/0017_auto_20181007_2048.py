# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 03:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='Contact_id',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
