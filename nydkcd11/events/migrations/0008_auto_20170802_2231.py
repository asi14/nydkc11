# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
    ]
