# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytu\u0142')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Odno\u015bnik')),
                ('text', models.TextField(verbose_name='Tre\u015b\u0107')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurs',
            },
        ),
    ]
