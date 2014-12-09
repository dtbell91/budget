from django.contrib import admin
from income.models import Person, Job, Pay

# Register your models here.
#start admin for Income
class JobInline(admin.TabularInline):
    model = Job
    extra = 2

class PayInline(admin.TabularInline):
    model = Pay
    extra = 12

class PersonAdmin(admin.ModelAdmin):
    {'fields': ['name']},
    inlines = [JobInline]

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['person', 'employer', 'expected_salary']}),
        ('Frequency Information',   {'fields': ['pay_frequency_unit', 'pay_frequency_count']}),
    ]
    inlines = [PayInline]

admin.site.register(Person, PersonAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Pay)
#end admin for Income
