from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date
from organizer.choices import *


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0)

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
