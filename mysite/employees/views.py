from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Employee
# Create your views here.

def employee_detail(request: HttpRequest, pk: int):
    # try:
    #     employee = Employee.objects.get(pk= pk)
    #     print(employee)
    #     return HttpResponse(employee.first_name)
    # except Employee.DoesNotExist:
    #     raise Http404("Employee does not exist!")

    employee = get_object_or_404(Employee, pk= pk)
    # return HttpResponse(employee.first_name)
    context = {
        "employee": employee
    }
    return render(request, 'employee_detail.html', context)