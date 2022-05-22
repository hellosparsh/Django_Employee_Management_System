from django.shortcuts import render, HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'emp_app/index.html')
def all_emp(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    print(context)
    return render(request,'emp_app/all_emp.html',context)
def add_emp(request):
    dep=Department.objects.all()
    role=Role.objects.all()
    context={
        'dep':dep,
        'role':role
    }
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone=int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully !!")
    else:
        return render(request,'emp_app/add_emp.html',context)
def remove_emp(request,emp_id=0):
    if emp_id!=0:
        try:
            emp_to_be_del=Employee.objects.get(id=emp_id)
            emp_to_be_del.delete()
            return HttpResponse("Deleted Successfully")
        except:
            return HttpResponse("Please Enter A Valid Employee ID !!")
    else:
        emp=Employee.objects.all()
        context={
            "emp":emp
        }
        return render(request,'emp_app/remove_emp.html',context)
def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emp=Employee.objects.all()
        if name:
            emp=emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name)) #__icontains search ingh and display sparsh singh, Q objects in django
        if dept:
            emp=emp.filter(dept__name__icontains=dept)
        if role:
            emp=emp.filter(role__name__icontains=role)
        context={
            'emp':emp
        }
        return render(request,'emp_app/all_emp.html',context)
    else:
        return render(request,'emp_app/filter_emp.html')
