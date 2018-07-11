# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('registration_num', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='BranchLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'branch_locations',
            },
        ),
        migrations.CreateModel(
            name='ProjectClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.Branches')),
                ('branch_locations', models.ManyToManyField(to='branches.BranchLocations')),
            ],
            options={
                'db_table': 'project_clients',
            },
        ),
    ]