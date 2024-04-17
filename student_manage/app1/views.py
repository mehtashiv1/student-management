from django.shortcuts import render, redirect
from app1.forms import EmployeeForm
from .models import StudentModel
# Create your views here.
def Home(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    data = StudentModel.objects.all()
    return render(request, 'index.html', {'form': form, 'data': data})


def Update(request, id):

    if request.method=="POST":
        data = StudentModel.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        data = StudentModel.objects.get(pk=id)
        form = EmployeeForm(instance=data)
    return render(request, 'update.html', {'form': form})


def Delete(request, id):
    a = StudentModel.objects.get(pk=id)
    a.delete()
    return redirect('/')

