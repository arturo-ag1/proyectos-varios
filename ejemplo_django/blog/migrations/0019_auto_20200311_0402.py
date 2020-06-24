# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-03-11 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200311_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Estado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Estado'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Estado'),
        ),
    ]