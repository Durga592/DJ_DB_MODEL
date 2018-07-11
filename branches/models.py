# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Branches(models.Model):
	name	=	models.CharField(max_length=250)
	registration_num	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'branches'

class BranchLocations(models.Model):
	name	=	models.CharField(max_length=250)
	address	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'branch_locations'

class ProjectClients(models.Model):
	name	=	models.CharField(max_length=250)
	branch_locations 	=	models.ManyToManyField(BranchLocations)
	branch 	=	models.ForeignKey(Branches)
	address	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'project_clients'