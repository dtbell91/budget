from django.contrib import admin
from bills.models import Company, Service, Bill
from income.models import Person, Employer, Job, Pay

#start admin for Bills
class ServiceInline(admin.TabularInline):
    model = Service
    extra = 2

class BillInline(admin.TabularInline):
    model = Bill
    extra = 2

class CompanyAdmin(admin.ModelAdmin):
    {'fields': ['name']},
    inlines = [ServiceInline]

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['company', 'name', 'cost']}),
        ('Frequency Information',   {'fields': ['frequency_unit', 'frequency_count']}),
    ]
    inlines = [BillInline]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Bill)
# end admin for Bills

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

class EmployerAdmin(admin.ModelAdmin):
    {'fields': ['name']},
    inlines = [JobInline]

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['person', 'employer', 'expected_salary']}),
        ('Frequency Information',   {'fields': ['pay_frequency_unit', 'pay_frequency_count']}),
    ]
    inlines = [PayInline]

admin.site.register(Person, PersonAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Pay)
#end admin for Income
