# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_remove_article_tpye'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Tpye',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Tpye'),
            preserve_default=False,
        ),
    ]
