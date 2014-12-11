from datetime import datetime
from django.db import models
from django.utils import timezone
from household.models import Household

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    household = models.ForeignKey(Household)
    
    def __unicode__(self):
        return self.name

class Job(models.Model):
    person = models.ForeignKey(Person)
    employer = models.CharField(max_length=100)
    expected_salary = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    DAY = 1
    WEEK = 7
    MONTH = 30.4375 #365.25 days divided by 12 months
    YEAR = 365.25 #average number of days, accounting for leap years
    FREQUENCY_CHOICES = (
        (DAY, 'Days'),
        (WEEK, 'Weeks'),
        (MONTH, 'Months'),
        (YEAR, 'Years'),
    )
    pay_frequency_unit = models.DecimalField(max_digits=8, decimal_places=4, choices=FREQUENCY_CHOICES, default=DAY)
    pay_frequency_count = models.IntegerField()
    
    def __unicode__(self):
        return self.person.__unicode__() + " - " + self.employer

class Pay(models.Model):
    job = models.ForeignKey(Job)
    date = models.DateField(default=datetime.now, blank=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    
    def __unicode__(self):
        return self.job.__unicode__() + " - " + self.date.strftime('%Y-%m-%d')
