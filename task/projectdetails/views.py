from django.shortcuts import redirect, render
import projectdetails
from .models import *
from .forms import *
from django.db import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_emp(request):
    employee = Employee.objects.all()
    return render(request, 'show_emp.html', {'emp':employee})

def show_proj(request):
    project = Project.objects.all()
    return render(request, 'show_proj.html', {'proj':project})

def show_ben_emp(request):
    benemp = Benchemp.objects.all()
    benemp.delete()
    a = Employee.objects.values_list('Employee_name', flat=True)
    b = Project.objects.values_list('Project_employees', flat=True)
    c = Benchemp.objects.values_list('Benchemp_name', flat=True)
    for i in a:
        if i not in b and i not in c:
            benemp = Benchemp.objects.create(Benchemp_name=i)
            benemp.save()    
    benemp = Benchemp.objects.all()
    return render(request, 'show_ben_emp.html', {'bemp':benemp})

def addemp(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            l = len(Employee.objects.values_list('Employee_name', flat=True))
            name = Employee.objects.values_list('Employee_name', flat=True)[l-1]
            form1 = Benchemp.objects.create(Benchemp_name=name)
            form1.save()
            return redirect('/show_emp')
    return render(request, 'add_employee.html',{'form':form})

def addproject(request):
    name = Benchemp.objects.all()
    if request.method == 'POST':
        id = int(request.POST["Project_id"])
        name = str(request.POST["Project_name"])
        emp = str(request.POST["Emp"])
        print(request.POST)
        project = Project(Project_id=id,Project_name=name,Project_employees=emp)
        project.save()
        l = Project.objects.values_list('Project_employees', flat=True)
        for i in range(len(l)):
            name = Project.objects.values_list('Project_employees', flat=True)[i]
            if name in Benchemp.objects.values_list('Benchemp_name', flat=True):
                benemp = Benchemp.objects.get(Benchemp_name=name)
                benemp.delete()
        return redirect('/show_proj')
    return render(request, 'add_project.html',{'empname':name})

def delete_emp(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show_emp')

def update_emp(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/show_emp')
    return render(request, 'update_emp.html', {'employee':employee})

def delete_proj(request,id):
    project = Project.objects.get(id=id)
    project.delete()
    benemp = Benchemp.objects.all()
    benemp.delete()
    a = Employee.objects.values_list('Employee_name', flat=True)
    b = Project.objects.values_list('Project_employees', flat=True)
    c = Benchemp.objects.values_list('Benchemp_name', flat=True)
    for i in a:
        if i not in b and i not in c:
            benemp = Benchemp.objects.create(Benchemp_name=i)
            benemp.save()    
    return redirect('/show_proj')

def update_proj(request,id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('/show_proj')
    return render(request, 'update_project.html', {'project':project})


   
