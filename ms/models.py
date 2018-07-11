# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name	=	models.CharField(max_length=250)
	cost	=	models.IntegerField()

	class Meta:
		db_table	=	'product'
class Customer(models.Model):
	name	=	models.CharField(max_length=250)
	address	=	models.TextField()

	class Meta:
		db_table	=	'customer'

class SalesOrder(models.Model):
	salesorder_type	=	[('online',"Online Payment"),('card',"Card Payment"), ('cod',"Cash on Delivery")]
	name			=	models.CharField(max_length=250)
	product 		=	models.ManyToManyField(Product)
	customer 		=	models.ForeignKey(Customer)
	sal_type		=	models.CharField(choices=salesorder_type, max_length=6)

	class Meta:
		db_table	=	'salesorders'