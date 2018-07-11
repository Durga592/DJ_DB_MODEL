# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Jobs(models.Model):
	name		=	models.CharField(max_length=250)
	job_type	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'jobs'

class Technologies(models.Model):
	name		=	models.CharField(max_length=250)
	version		=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'technologies'

class Clients(models.Model):
	name		=	models.CharField(max_length=250)
	technology	=	models.ManyToManyField(Technologies)
	job 		=	models.ForeignKey(Jobs)
	address		=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'clients'