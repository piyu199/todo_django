from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    if request.method=='POST':
        task=request.POST["task"]
        task=Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    tasks=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        tasks.task=new_task
        tasks.save()
        return redirect('home')
    else:
        context={
            "tasks":tasks,
        }
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')

      
