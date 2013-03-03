from django.db import models
from django.contrib import admin

class User(models.Model):
	name 	  		= models.CharField(max_length=255)
	address 		= models.CharField(max_length=255)
	email	  		= models.EmailField(max_length=255)
	bio     		= models.TextField()
	philosophy 	= models.TextField()
	goals			= models.CharField(max_length=255)
	links			= models.ForeignKey('Link')

class Campaign(models.Model):
	position				= models.CharField(max_length=255)
	# fiveStances 		= models.ManyToManyField()
	first100Days		= models.CharField(max_length=255)
	whyBestCandidate	= models.CharText()
	videoURL				= models.CharField(max_length=255)
	fundingThreshold	= models.DecimalField(max_digits=8, decimal_places=0)
	campaignEndDate	= models.DateField()
	electionEndDate	= models.DateField()
	amountPledged		= models.DecimalField(max_digits=8, decimal_places=0)
	numberSupporters  = models.DecimalField(max_digits=8, decimal_places=0)
	links					= models.ForeignKey('Link')

class Link(models.Model):
	title		=	models.CharField(max_length=255)
	URL		=  models.CharField(max_length=255)
	
models = [User, Campaign, Link]

map(admin.site.register,models)