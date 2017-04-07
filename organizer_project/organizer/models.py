from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
	user = models.ForeignKey(User)
	product = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	purchase_date = models.DateField(auto_now=False)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return '{}| |{}| |{}| |{}| |{}|'.format(self.user, self.product, self.price, 
				self.purchase_date, self.description)

