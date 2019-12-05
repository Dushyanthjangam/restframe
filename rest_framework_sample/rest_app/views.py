from django.shortcuts import render
from .models import EmployeeRegistration

# Create your views here.
def loginpage(request):
    return render(request,'one.html')


def savingDate(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    image=request.FILES['image']
    EmployeeRegistration(employeeid=id,empname=name,empsalary=salary,empimg=image).save()
    return render(request,'one.html',{'message':" Employe Details registered "})


def employeeDetails(request):
    viewDetails=EmployeeRegistration.objects.all()
    return render(request,'two.html',{'viewDeatils':viewDetails})


def backtomainpage(request):
    return loginpage(request)