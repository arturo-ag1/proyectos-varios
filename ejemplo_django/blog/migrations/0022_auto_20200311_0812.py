# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-03-11 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_orden_ocultar'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=400, null=True)),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('apaterno', models.CharField(blank=True, max_length=200, null=True)),
                ('amaterno', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=400, null=True)),
                ('telefono', models.CharField(blank=True, max_length=400, null=True)),
                ('rfc', models.CharField(blank=True, max_length=400, null=True)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.StatusTecnico')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=400, null=True)),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='tecnico',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.TipoTecnico'),
        ),
    ]
