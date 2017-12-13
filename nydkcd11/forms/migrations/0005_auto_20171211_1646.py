# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20170619_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='papers',
            options={'verbose_name': 'Application Resources'},
        ),
        migrations.AlterField(
            model_name='papers',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Title of Paper/Form/Application'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='url',
            field=models.CharField(max_length=300, verbose_name='URL to Paper/Form/Application'),
        ),
    ]