# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-24 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_fix_url_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='text_version',
            field=models.TextField(default=''),
        ),
    ]