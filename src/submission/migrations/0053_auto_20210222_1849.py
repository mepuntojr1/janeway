# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-22 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0052_auto_20210222_1845'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sectiontranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sectiontranslation',
            name='master',
        ),
        migrations.AlterModelManagers(
            name='section',
            managers=[
            ],
        ),
        migrations.DeleteModel(
            name='SectionTranslation',
        ),
    ]