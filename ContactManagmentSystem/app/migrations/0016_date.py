# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20181007_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_type', models.CharField(max_length=30, null=True)),
                ('Date', models.DateTimeField(null=True)),
                ('Contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Contacts')),
            ],
        ),
    ]
