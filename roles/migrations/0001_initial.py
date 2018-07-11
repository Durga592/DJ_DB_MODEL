# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('role_type', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('mailid', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='modules',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.Roles'),
        ),
        migrations.AddField(
            model_name='modules',
            name='user',
            field=models.ManyToManyField(to='roles.Users'),
        ),
    ]