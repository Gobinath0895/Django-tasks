from django.db import models

# Create your models here.

class emp(models.Model):
    EmpNo = models.IntegerField()
    EmpName = models.CharField(max_length = 20)
    Empsalary = models.CharField()
    EmpAddress = models.FloatField(max_length = 100)
    
