# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170711_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='show_screen',
            field=models.BooleanField(default=False, verbose_name=b'Show on Events List?'),
        ),
    ]
