from datetime import datetime
from datetime import timedelta
from django.db import models
from django.db.models import Avg, Sum
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    company_name = models.CharField(max_length=200)
    service_name = models.CharField(max_length=200)
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
    
    def frequency_indays(self):
        days = self.frequency_unit * self.frequency_count
        return round(days)
    
    def frequency_peryear(self):
        return self.YEAR // float(self.frequency_indays())
    
    def expected_next_bill(self):
        return self.bill_set.order_by('date_paid').last().date_paid + timedelta(days = self.frequency_indays())
    
    def expected_next_bill_indays(self):
        return self.expected_next_bill().toordinal() - datetime.today().toordinal()
    
    def __unicode__(self):
        return self.company_name + " - " + self.service_name
    
    def average_bill_bycount(self, count):
        average = self.bill_set.order_by('date_paid').reverse()[:count].aggregate(Avg('cost'))
        return average
    
    def average_bill_bydays(self, past_days):
        enddate = datetime.today()
        startdate = enddate - timedelta(days = past_days)
        average = self.bill_set.filter(date_paid__range = [startdate, enddate]).aggregate(Avg('cost'))
        return average
    
    def sum_paid(self, past_days):
        sum = 0
        enddate = datetime.today()
        startdate = enddate - timedelta(days = past_days)
        sum = self.bill_set.filter(date_paid__range=[startdate, enddate]).aggregate(Sum('cost'))
        return sum
    
    def cost_perday(self):
        cost = float(self.cost) / self.frequency_indays()
        return round(cost,2)

class Bill(models.Model):
    service = models.ForeignKey(Service)
    date_paid = models.DateField(default=datetime.now, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __unicode__(self):
        return self.service.__unicode__() + " - " + self.date_paid.strftime('%Y-%m-%d')
