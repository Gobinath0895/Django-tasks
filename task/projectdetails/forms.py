from django import forms
from projectdetails.models import Benchemp, Project, Employee

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
class BenchempForm(forms.ModelForm):
    class Meta:
        model = Benchemp
        fields = '__all__'