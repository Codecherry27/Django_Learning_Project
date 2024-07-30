from django.contrib import admin
from .models import company,employee

# Register your models here.
class companyadmin(admin.ModelAdmin):
    list_display=('name','location','type_of_company')
    search_fields = ('name',)

class employeeadmin(admin.ModelAdmin):
    list_display=('name','email','Company')
    search_fields = ('name',)
    list_filter = ('Company',)

admin.site.register(company,companyadmin)
admin.site.register(employee,employeeadmin)

