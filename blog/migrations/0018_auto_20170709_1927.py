# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20170709_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to=b''),
        ),
    ]