from django.db import models
from django.urls import reverse

class Deposit(models.Model):

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField()
    interest = models.FloatField()

    def get_absolute_url(self) :
        return reverse ('home')