from django.shortcuts import render
from django.http import HttpResponse
import time

def home(request):
    return render(request,'home.html', {'name':'Gobinath'})

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    res = a + b
    res1 = abs(a - b)
    res2 = a/b
    res3 = a*b
    date1 = time.strftime("%H:%M:%S", time.localtime())  
    return render(request,'result.html', {'result':res,'result1': res1,'result2':res2,'result3':res3,'Date':date1})


