# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-01-17 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200116_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='alumno',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='blog.Alumno'),
            preserve_default=False,
        ),
    ]