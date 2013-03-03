from django.db import models
from django.contrib import admin

class Campaign(models.Model):
	position				= models.CharField(max_length=255)
	# fiveStances 		= models.ForeignKey('Stance')
	first100Days		= models.TextField()
	whyBestCandidate	= models.TextField()
	videoURL				= models.CharField(max_length=255)
	fundingThreshold	= models.DecimalField(max_digits=8, decimal_places=0)
	campaignEndDate	= models.DateField()
	electionEndDate	= models.DateField()
	amountPledged		= models.DecimalField(max_digits=8, decimal_places=0)
	numberSupporters  = models.DecimalField(max_digits=8, decimal_places=0)
	# links					= models.ForeignKey('Link')

class Link(models.Model):
	title		=	models.CharField(max_length=255)
	URL		=  models.CharField(max_length=255)
	
class Stance(models.Model):
	text	= models.TextField()

models = [Campaign, Link, Stance]

map(admin.site.register,models)