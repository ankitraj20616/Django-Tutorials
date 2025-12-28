from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request: HttpRequest):
    tasks_uncompleted = Task.objects.filter(is_completed= False).order_by('-updated_at')
    tasks_completed = Task.objects.filter(is_completed= True).order_by('-updated_at')
    context = {
        "tasks_uncompleted": tasks_uncompleted,
        "tasks_completed": tasks_completed
    }
    return render(request, "home.html", context)