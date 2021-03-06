# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_division_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='school_photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='division',
            name='image',
            field=models.ImageField(upload_to='division_photos/'),
        ),
    ]
