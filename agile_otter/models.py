from django.db import models
from django.contrib import admin

class User(models.Model):
	name 	  = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	email	  = models.CharField(max_length=255)
	
admin.site.register(User)