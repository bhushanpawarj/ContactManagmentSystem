# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-07 23:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181007_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='Contact_id',
        ),
        migrations.RemoveField(
            model_name='date',
            name='Contact_id',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='Contact_id',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
