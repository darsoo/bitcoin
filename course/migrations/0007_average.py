# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Average',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bids', models.CharField(max_length=255, verbose_name='Bids')),
                ('asks', models.CharField(max_length=255, verbose_name='Ask')),
            ],
        ),
    ]
