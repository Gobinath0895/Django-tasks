from django.shortcuts import render
from django.http import HttpResponse

def note(request):
    return render(request,'home.html',{'name':'Welcome to the Homepage'})
def add(request):
    a = float(request.POST['num1'])
    b = float(request.POST['num2'])
    res = a+b
    return render(request, 'result.html', {'result': res})