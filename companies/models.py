# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name	=	models.CharField(max_length=250)
	address	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'company'

class CompanyLocations(models.Model):
	name	=	models.CharField(max_length=250)
	address	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'company_locations'

class Employees(models.Model):
	name		=	models.CharField(max_length=250)
	company 	=	models.ManyToManyField(Company)
	company_location 	=	models.ForeignKey(CompanyLocations)
	designation	=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'employees'