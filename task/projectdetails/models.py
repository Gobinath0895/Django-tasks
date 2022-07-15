from msilib.schema import Class
from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id = models.IntegerField()
    Employee_name = models.CharField(max_length = 30)
    Employees_address = models.CharField(max_length = 100)
    Employee_phone_number = models.BigIntegerField()
    
class Project(models.Model):
    Project_id = models.IntegerField()
    Project_name = models.CharField(max_length = 30)
    Project_employees = models.CharField(max_length = 100)

class Benchemp(models.Model):
    Benchemp_name = models.CharField(max_length = 30)