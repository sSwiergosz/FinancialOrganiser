from django.db import models
from django.contrib.auth.models import User

from datetime import date
from organizer.choices import *

class Transaction(models.Model):
	user = models.ForeignKey(User)
	category = models.CharField(choices=NAME_CHOICES, max_length=20)
	product = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	purchase_date = models.DateField(auto_now=False, default=date.today)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return '{0}| |{1}| |{2}| |{3}| |{4}|'.format(self.user, self.product, self.price, 
				self.purchase_date, self.description)
