# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-01-16 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='grado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Grado'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Grupo'),
        ),
    ]