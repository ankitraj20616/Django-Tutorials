from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from employees.models import Employee

def root(request: HttpRequest):
    return HttpResponse("<h1>Welcome To Root Page</h1>")

def home(request: HttpRequest):
    employees = Employee.objects.all()
    context = {
        "employees": employees,
    }
    return render(request, 'home.html', context)