from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Opportunity(models.Model):
	opportunity_name = models.CharField(max_length=200)
	client_name = models.CharField(max_length=200)
	solicitation_date = models.DateTimeField('solicitation date')
	response_date = models.DateTimeField('response due date')
	def __str__(self):
		return self.opportunity_name
