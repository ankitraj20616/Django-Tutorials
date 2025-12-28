from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task

# Create your views here.
def add_task(request: HttpRequest):
    task = request.POST['task']
    Task.objects.create(task= task)
    return redirect("home")

def mark_as_done(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk= pk)
    task.is_completed = True
    task.save()
    return redirect("home")

def mark_as_undone(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk= pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request: HttpRequest, pk: int):
    get_task = get_object_or_404(Task, pk= pk)
    if request.method == "POST":
        new_task = request.POST["task"]
        get_task.task = new_task
        get_task.is_completed = False
        get_task.save()
        return redirect('home')
    else:
        context = {
            "get_task": get_task
        }
        return render(request, 'edit_task.html', context)
    
def delete_task(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk= pk)
    task.delete()
    return redirect('home')
