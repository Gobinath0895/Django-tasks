from django.contrib import admin
from projectdetails.models import Employee,Project,Benchemp

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list = ['Employee_id', 'Employee_name', 'Employees_address', 'Employee_phone_number']
class ProjectAdmin(admin.ModelAdmin):
    list = ['Project_id','Project_name', 'Project_employees']
    
class BenchempAdmin(admin.ModelAdmin):
    list = ['Benchemp_name']
