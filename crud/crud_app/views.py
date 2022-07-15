from django.shortcuts import redirect, render
from crud_app.models import Student
from crud_app.forms import StudentForm

# Create your views here.
def retrieve_view(request):
    stnt = Student.objects.all()
    return render(request, 'result.html',{'student':stnt})
def create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')        
    return render(request, 'create.html', {'form': form})
def delete(request,sno):
    stnt = Student.objects.get(sno=sno)
    stnt.delete()
    return redirect('/check')
def update(request,sno):
    stnt = Student.objects.get(sno=sno)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=Student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'update.html',{'student':stnt})
    