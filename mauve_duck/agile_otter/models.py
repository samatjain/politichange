from django.db import models
from django.contrib import admin

class Link(models.Model):
	title		=	models.CharField(max_length=255)
	URL		=  models.CharField(max_length=255)

class Campaign(models.Model):
	position				= models.CharField(max_length=255)
	fiveStances 		= models.ForeignKey('Stance', blank=True,null=True)
	first100Days		= models.TextField(blank=True,null=True)
	whyBestCandidate	= models.TextField(blank=True,null=True)
	videoURL				= models.CharField(max_length=255,blank=True,null=True)
	fundingThreshold	= models.DecimalField(max_digits=8, decimal_places=0)
	campaignEndDate	= models.DateField()
	electionEndDate	= models.DateField()
	amountPledged		= models.DecimalField(max_digits=8, decimal_places=0,blank=True,null=True)
	numberSupporters  = models.DecimalField(max_digits=8, decimal_places=0,blank=True,null=True)
	links					= models.ForeignKey(Link,blank=True,null=True)

class Stance(models.Model):
	text	= models.TextField()

class Participant(models.Model):
	name 	  		= models.CharField(max_length=255)
	address 		= models.CharField(max_length=255)
	email	  		= models.EmailField(max_length=255)
	bio     		= models.TextField()
	philosophy 	= models.TextField(blank=True,null=True)
	goals			= models.CharField(max_length=255)
	links			= models.ForeignKey(Link,blank=True,null=True)

models = [Campaign, Link, Stance, Participant]

map(admin.site.register,models)