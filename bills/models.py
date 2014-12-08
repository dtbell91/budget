from datetime import datetime
from datetime import timedelta
from django.db import models
from django.db.models import Avg
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Service(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
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
    frequency_unit = models.DecimalField(max_digits=8, decimal_places=4, choices=FREQUENCY_CHOICES, default=DAY)
    frequency_count = models.IntegerField()
    def __unicode__(self):
        return self.company.__unicode__() + " - " + self.name
    
    def average_bill(self, count):
        average = self.bill_set.order_by('date_paid').reverse()[:count].aggregate(Avg('cost'))
        return average
    
    def sum_paid(self, past_days):
        sum = 0
        enddate = datetime.today()
        startdate = enddate - timedelta(days=past_days)
        for b in self.bill_set.filter(date_paid__range=[startdate, enddate]).values_list('cost'):
            sum += b[0]
        return sum

class Bill(models.Model):
    service = models.ForeignKey(Service)
    date_paid = models.DateField(default=datetime.now, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __unicode__(self):
        return self.service.__unicode__() + " - " + self.date_paid.strftime('%Y-%m-%d')
