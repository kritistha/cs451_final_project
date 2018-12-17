from django.db import models

from django.conf import settings 

APP_LOCATION = settings.DEFAULT_LOCATION
class Job(models.Model):
	title = models.CharField(max_length=128)
	salary = models.IntegerField()
	address = models.CharField(max_length=128)
	lat = models.FloatField()
	lon = models.FloatField()
	
	def __str__(self):
		return self.title
