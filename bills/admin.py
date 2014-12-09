from django.contrib import admin
from bills.models import Service, Bill

#start admin for Bills
class BillInline(admin.TabularInline):
    model = Bill
    extra = 2

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['company', 'name', 'cost']}),
        ('Frequency Information',   {'fields': ['frequency_unit', 'frequency_count']}),
    ]
    inlines = [BillInline]

admin.site.register(Service, ServiceAdmin)
admin.site.register(Bill)
# end admin for Bills
