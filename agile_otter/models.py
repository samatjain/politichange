from django.db import models

class User(models.Model):
	name 	  = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	email	  = models.CharField(max_length=255)
	
