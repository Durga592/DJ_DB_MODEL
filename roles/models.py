# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	name		=	models.CharField(max_length=250)
	password	=	models.CharField(max_length=250)
	mailid		=	models.CharField(max_length=250)

	class Meta:
		db_table	=	'users'

class Roles(models.Model):
	name		=	models.CharField(max_length=250)
	role_type	=	models.CharField(max_length=250)		

	class Meta:
		db_table	=	'roles'

class Modules(models.Model):
	name		=	models.CharField(max_length=250)
	user 		=	models.ManyToManyField(Users)
	role 		=	models.ForeignKey(Roles)

	class Meta:
		db_table	=	'modules'